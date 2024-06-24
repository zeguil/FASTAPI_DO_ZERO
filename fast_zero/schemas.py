from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class Menssage(BaseModel):
    message: str


class UserPublic(BaseModel):
    username: str
    email: EmailStr
