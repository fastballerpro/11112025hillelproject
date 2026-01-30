from pydantic import BaseModel, EmailStr, ConfigDict


class UserPasswordSchema(BaseModel):
    password: str


class UserBaseFieldsSchemas(BaseModel):
    email: EmailStr
    name: str

    model_config = ConfigDict(
        str_strip_whitespace=True,
    )


class RegisterUserSchema(UserBaseFieldsSchemas, UserPasswordSchema):
    pass