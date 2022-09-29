from pydantic import BaseModel

class UserSchema(BaseModel):
    email: str
    first_name: str
    last_name: str
    user_type: str

    class Config:
        orm_mode = True