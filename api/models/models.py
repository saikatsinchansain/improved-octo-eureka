from pydantic import BaseModel

class Profile(BaseModel):
    uuid: str
    fname: str
    lname: str

    class Config:
        orm_mode = True