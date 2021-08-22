from pydantic import BaseModel
# from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
# from sqlalchemy.orm import relationship

# from sql import database


# class Profile_Table(database.Base):
#     __tablename__ = "profiles"

#     uuid = Column(String, primary_key=True, index=True)
#     fname = Column(String)
#     lname = Column(String)
    

class Profile(BaseModel):
    uuid: str
    fname: str
    lname: str

    # class Config:
    #     orm_mode = True