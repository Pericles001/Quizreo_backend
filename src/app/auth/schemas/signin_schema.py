from src.app.core.base_schema import ReadModelSchema


class SigninSchema(ReadModelSchema):
    username: str
    password: str
