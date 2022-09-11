from fastapi import APIRouter, Depends
from src.app.core import settings
from src.app.auth.services import auth_service
from src.app.auth.services.auth_service import auth_service
from src.app.user.routers.user_router import router as user_router
from src.app.auth.routers.auth_router import router as auth_router
from src.app.quizreo.routers.answer_router import router as answer_router


base_router = APIRouter(prefix=settings.API_V1_STR)

resource_router = APIRouter(
    prefix="/resources", 
    dependencies=[Depends(auth_service.get_current_user)]
)

resource_router.include_router(user_router)
resource_router.include_router(answer_router)


base_router.include_router(auth_router)
base_router.include_router(resource_router)

