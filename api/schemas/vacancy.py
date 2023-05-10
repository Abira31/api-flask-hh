from pydantic import BaseModel

class VacancyBase(BaseModel):
    id: int
    name: str
    class Config:
        orm_mode = True

class VacancyDetailBase(BaseModel):
    name: str
    class Config:
        orm_mode = True