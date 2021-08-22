from fastapi import APIRouter
from queries import queries
from models import models

router = APIRouter(
    prefix="/profiles",
    tags=["profiles"],
    responses={404: {"description": "Not found"}},
)

#A route to return all of the available entries in our catalog.
@router.get('/all', summary='Get list of all profiles')
async def api_all_profiles():
    return queries.all_profiles()

@router.get('/{uuid}',summary='Get profile')
async def api_profile_by_uuid(uuid):
    return queries.profile_by_uuid(uuid)

@router.post('/', summary='Insert new profile')
async def insert_profile(profile: models.Profile):
    return {"uuid": profile.uuid, "fname": profile.fname, "lname": profile.lname}