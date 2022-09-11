import base64
import uvicorn
from fastapi import Depends, FastAPI
from src.app.auth.schemas.signin_schema import SigninSchema
from src.app.auth.services.auth_service import auth_service
from src.app.core import settings
from src.app.core.basic_auth import basic_auth
from src.app.core.base_router import base_router
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.utils import get_openapi
from fastapi.templating import Jinja2Templates
from fastapi import Request
from starlette.responses import RedirectResponse, Response
from fastapi.encoders import jsonable_encoder
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html
)
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from src.app.core.basic_auth import BasicAuth

from src.app.helpers.enums.path_operation_tag_enum import PathOperationTag

favicon_path = "/public/static/images/shell.ico"

templates = Jinja2Templates(directory="src/templates")

origins = ["*"]

api_metadata = {
    "version": "0.0.1",
    "description": """
        QUIZREO API, webservices empowering the project QUIZREO.
    """,
    "terms_of_service": "pericles.com",
    "contact": {
        "name": "pericles001",
        "url": "https://pericles001.com",
        "email": "pericles001@adjovi.com",
    },
    "license_info": {
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    "tags_metadata": [{ "name": path_operation_tag.value, "description": f"{path_operation_tag.value.lower()} specific operations are here" } for path_operation_tag in PathOperationTag],
}

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=api_metadata["version"],
    description=api_metadata["description"],
    terms_of_service=api_metadata["terms_of_service"],
    contact=api_metadata["contact"],
    license_info=api_metadata["license_info"],
    openapi_tags=api_metadata["tags_metadata"],
    docs_url=None,
    redoc_url=None,
)
app.mount("/public", StaticFiles(directory="public"), name="static")
app.include_router(base_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "DELETE", "PUT", "HEAD", "OPTIONS"],
    allow_headers=[
        "Access-Control-Allow-Headers",
        "Content-Type",
        "Authorization",
        "Access-Control-Allow-Origin",
        "Set-Cookie",
        "x-requested-with",
    ],
)


@app.get("/", include_in_schema=False)
async def homepage(request: Request):
    swagger_doc_login_url = "/swagger-doc-login"
    redocli_doc_login_url = "/redocli-doc-login"
    project_name = settings.PROJECT_NAME
    return templates.TemplateResponse(
        "note.html", 
        {
            "request": request, 
            "project_name": project_name,
            "swagger_doc_login_url": swagger_doc_login_url,
            "redocli_doc_login_url": redocli_doc_login_url,
        }
    )


@app.get("/openapi.json", include_in_schema=False)
async def get_open_api_endpoint(user=Depends(auth_service.get_current_open_api_user)):
    return JSONResponse(
        get_openapi(title=app.title + " - SWAGGER UI", version=1, routes=app.routes)
    )


@app.get(f"{settings.API_DOCS_BASE_URL}/swagger", include_in_schema=False)
async def custom_swagger_ui_html(
    user=Depends(auth_service.get_current_open_api_user),
):
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=f"{app.title} - SWAGGER UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="/public/static/js/swagger-ui-bundle.js",
        swagger_css_url="/public/static/css/swagger-ui.css",
        swagger_ui_parameters={"syntaxHighlight.theme": "tomorrow-night"},
        swagger_favicon_url=favicon_path,
    )


@app.get(f"{settings.API_DOCS_BASE_URL}/redoc", include_in_schema=False)
async def custom_redoc_html(user=Depends(auth_service.get_current_open_api_user)):
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=f"{app.title} - REDOCLI UI",
        redoc_js_url="/public/static/js/redoc.standalone.js",
        redoc_favicon_url=favicon_path,
    )


@app.get("/swagger-doc-login", include_in_schema=False)
async def login_into_swagger_docs(*, auth: BasicAuth = Depends(basic_auth)):
    if not auth:
        response = Response(headers={"WWW-Authenticate": "Basic"}, status_code=401)
        return response
    try:
        decoded = base64.b64decode(auth).decode("ascii")
        username, _, password = decoded.partition(":")
        credentials = SigninSchema(username=username, password=password)
        access_token = auth_service.authenticate_open_api_user(user_credentials=credentials)["access_token"]
        token = jsonable_encoder(access_token)
        response = RedirectResponse(url=f"{settings.API_DOCS_BASE_URL}/swagger")
        response.set_cookie(
            "Authorization",
            value=f"Bearer {token}",
            httponly=True,
            expires=(10 * 365 * 24 * 60 * 60),
        )
        return response
    except:
        response = Response(headers={"WWW-Authenticate": "Basic"}, status_code=401)
        return response

@app.get("/redocli-doc-login", include_in_schema=False)
async def login_into_redocli_docs(*, auth: BasicAuth = Depends(basic_auth)):
    if not auth:
        response = Response(headers={"WWW-Authenticate": "Basic"}, status_code=401)
        return response
    try:
        decoded = base64.b64decode(auth).decode("ascii")
        username, _, password = decoded.partition(":")
        credentials = SigninSchema(username=username, password=password)
        access_token = auth_service.authenticate_open_api_user(user_credentials=credentials)["access_token"]
        token = jsonable_encoder(access_token)
        response = RedirectResponse(url=f"{settings.API_DOCS_BASE_URL}/redoc")
        response.set_cookie(
            "Authorization",
            value=f"Bearer {token}",
            httponly=True,
            expires=(10 * 365 * 24 * 60 * 60),
        )
        return response
    except:
        response = Response(headers={"WWW-Authenticate": "Basic"}, status_code=401)
        return response

@app.get("/logout", include_in_schema=False)
async def logout():
    response = RedirectResponse(url=f"{settings.API_DOCS_BASE_URL}/redoc")
    response.delete_cookie("Authorization")
    return response

if __name__ == "__main__":
    if settings.PROD_MODE == True:
        uvicorn.run("src.main:app", host="0.0.0.0", port=settings.PORT)
    else:
        uvicorn.run("src.main:app", host="0.0.0.0", port=settings.PORT, reload=True)
