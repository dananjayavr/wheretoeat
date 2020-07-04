import requests
import config


# Yelp docs: https://www.yelp.com/developers/documentation/v3/business_search

def fetch_nearest_restaurants():
    header = {'Authorization': 'Bearer ' + config.YELP_API_KEY}
    payload = {
        "latitude": config.OFFICE_LAT,
        "longitude": config.OFFICE_LON,
        "category": "restaurants",
        "radius": 500,
        "sort_by": "distance",
        "open_now": "true"
    }
    url = 'https://api.yelp.com/v3/businesses/search'

    r = requests.get(url, params=payload, headers=header).json()

    businesses = r['businesses']
    formatted_businesses = []
    for business in businesses:
        if "price" in business:
            formatted_businesses.append(
                f"{business['name']} / {business['location']['address1']} / {business['rating']} / {business['price']}")
            # print(f"{business['url']}")
        else:
            formatted_businesses.append(
                f"{business['name']} / {business['location']['address1']} / {business['rating']}")
            # print(f"{business['url']}")

    return formatted_businesses

