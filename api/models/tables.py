from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from .models import ProfileVO

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


def get_all_profile(db: Session):
    return db.query(Profile).all()

def get_profile(db: Session, uuid: str):
    return db.query(Profile).filter(Profile.uuid == uuid).all()

def create_profile(db: Session, profile: ProfileVO):
    db_profile = Profile(profile.uuid,profile.fname,profile.lname)
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile
    #return profile