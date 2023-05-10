from pydantic import BaseModel
from api.schemas.role import RolesBase

class UserBase(BaseModel):
    id : int
    email : str
    first_name : str
    last_name : str
    phone : str
    roles: list[RolesBase]
    class Config:
        orm_mode = True


class UserDetailBase(BaseModel):
    email: str
    is_active: bool
    first_name: str
    last_name: str
    phone: str
    roles: list[RolesBase]
    is_admin: bool

    class Config:
        orm_mode = True