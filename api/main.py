from fastapi import FastAPI
from database import fetch_query
from pydantic import BaseModel

app = FastAPI()

class Profile(BaseModel):
    uuid: str
    fname: str
    lname: str

# Create some test data for our catalog in the form of a list of dictionaries.
def all_profiles():
    response = fetch_query('(SELECT * FROM profiles)')
    return response

def profile_by_uuid(uuid):
    response = fetch_query('(SELECT * FROM profiles WHERE uuid = "%s")'%(uuid))
    return response

# A route to return all of the available entries in our catalog.
@app.get('/api/v1/resources/profiles/all')
def api_all_profiles():
    return all_profiles()

@app.get('/api/v1/resources/profiles/{uuid}')
def api_profile_by_uuid(uuid):
    print("UUID sent = {}".format(uuid))
    return profile_by_uuid(uuid)

@app.post('/api/v1/resources/profile/')
def insert_profile(profile: Profile):
    return {"uuid": profile.uuid, "fname": profile.fname, "lname": profile.lname}