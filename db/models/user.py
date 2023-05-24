from pydantic import BaseModel
from typing import Optional


class User (BaseModel):
    id:  Optional[str]
    firstname: str
    lastname: str
    email: str
    avatar: str
