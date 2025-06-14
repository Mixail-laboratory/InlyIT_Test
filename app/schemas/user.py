from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    full_name: str
    email: EmailStr


class UserCreate(UserBase):
    password: str
    is_admin: bool


class UserRead(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True
