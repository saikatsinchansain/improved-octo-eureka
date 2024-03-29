from fastapi import APIRouter
from models import models,tables
from sql import database
from base_logger import logger


router = APIRouter(
    prefix="/profiles",
    tags=["profiles"],
    responses={404: {"description": "Not found"}},
)

#A route to return all of the available entries for profile.
@router.get('/all', summary='Get list of all profiles')
async def api_all_profiles():
    logger.info("Invoking api_all_profiles")
    return tables.get_all_profile(database.Session())

#A route to return matching entries for profile.
@router.get('/{uuid}',summary='Get profile')
async def api_profile_by_uuid(uuid):
    logger.info("Invoking api_profile_by_uuid with uuid:{}".format(uuid))
    return tables.get_profile(database.Session(),uuid)

#A route to add new profile.
@router.post('/', summary='Insert new profile')
async def insert_profile(profile: models.ProfileVO):
    logger.info("Invoking insert_profile with request:{}".format(profile))
    return tables.create_profile(database.Session(),profile)