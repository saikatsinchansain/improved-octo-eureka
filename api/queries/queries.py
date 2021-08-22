from .dbconnection import fetch_query
 
def all_profiles():
    response = fetch_query('(SELECT * FROM profiles)')
    return response

def profile_by_uuid(uuid):
    response = fetch_query('(SELECT * FROM profiles WHERE uuid = "%s")'%(uuid))
    return response
