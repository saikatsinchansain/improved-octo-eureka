from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

#Standard way of mapping database objects. Need to explore integration with pydantic

from sql import database
class Profile(database.Base):
    __tablename__ = "profiles"

    uuid = Column(String, primary_key=True, index=True)
    fname = Column(String)
    lname = Column(String)
    
    def __init__(self,uuid,fname,lname):
        self.uuid = uuid
        self.fname = fname
        self.lname = lname
