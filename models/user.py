from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
class UserBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
class UserCreate(UserBase):
    password: str = Field(..., min_length=8)
class UserOut(UserBase):
    id: int
    roles: List[str] = []
class UserInDB(UserOut):
    hashed_password: str
class UserLogin(BaseModel):
    email: EmailStr
    password: str
class UserRoleUpdate(BaseModel):
    roles: List[str] = Field(
        ...,
        min_items=1,
        description="List of roles to assign to the user. Valid values: 'user', 'admin', 'moderator'."
    )