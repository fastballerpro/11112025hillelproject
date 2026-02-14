from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime

class UserPasswordSchema(BaseModel):
    password: str


class UserBaseFieldsSchemas(BaseModel):
    email: EmailStr
    name: str

    model_config = ConfigDict(
        str_strip_whitespace=True,
    )


class UserResponseSchema(UserBaseFieldsSchemas):
    id: int
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True,
        str_strip_whitespace=True,
    )


class RegisterUserSchema(UserBaseFieldsSchemas, UserPasswordSchema):
    pass


class NoteCreateSchema(BaseModel):
    name: str
    content: str
    
    model_config = ConfigDict(
        str_strip_whitespace=True,
    )


class NoteResponseSchema(NoteCreateSchema):  
    id: int
    user_id: int
    created_at: datetime  
    
    model_config = ConfigDict(
        from_attributes=True,  
        str_strip_whitespace=True,
    )