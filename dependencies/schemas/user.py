from pydantic import BaseModel

class User(BaseModel):
    email: str
    first_name: str
    last_name: str
    user_type: str

    class Config:
        orm_mode = True