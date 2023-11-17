# curl "https://test.api.amadeus.com/v1/security/oauth2/token"      -H "Content-Type: application/x-www-form-urlencoded"      -d "grant_type=client_credentials&client_id=UgvkvcINTG93c4hNbGGY4LN3nRxrk9Ex&client_secret=TZLqA7rukbLdWSSw"

#         {
#             "type": "amadeusOAuth2Token",
#             "username": "jorge@domingues.tech",
#             "application_name": "demoamadeushotel",
#             "client_id": "UgvkvcINTG93c4hNbGGY4LN3nRxrk9Ex",
#             "token_type": "Bearer",
#             "access_token": "UeBbIzOk8ip5Mv1sAggBay8C1gQv",
#             "expires_in": 1799,
#             "state": "approved",
#             "scope": ""
#         }

# GET EXAMPLE:  curl "https://test.api.amadeus.com/v1/reference-data/locations/hotels/by-city?cityCode=LON"      -H "Authorization: Bearer RMvQjG3TK1ixyYXf2DG6dnVqprUx"


import requests

AMADEUS_API_KEY = '7GQutU8AA0jsgcg3Nj0OOrn3UAzl'

def search_hotels(location):
    base_url = 'https://test.api.amadeus.com/v1/reference-data/locations/hotels/by-city'
    params = {
        'cityCode': location,  # City or location code,
    }
    headers = {
        'Authorization': f'Bearer {AMADEUS_API_KEY}',
    }

    response = requests.get(base_url, params=params, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        # Handle errors gracefully
        return None



