from pydantic import BaseModel
from datetime import datetime

class ResumesBase(BaseModel):
    salary : float
    description : str
    publication_date : datetime
    is_active : bool
