from pydantic import BaseModel

class ProfileVO(BaseModel):
    uuid: str
    fname: str
    lname: str

    class Config:
        orm_mode = True
