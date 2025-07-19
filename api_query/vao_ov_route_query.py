import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
ACCESS_ID = os.getenv("ACCESS_ID")
BASE_URL = "https://routenplaner.verkehrsauskunft.at/vao/restproxy/v1.11.0/"

def resolve_location(name):
    params = {
        "accessId": ACCESS_ID,
        "input": name,
        "format": "json",
        "maxLocations": 1
    }
    response = requests.get(BASE_URL + "locations", params=params)
    return response.json()["locations"][0]["id"]

def get_trip(origin_id, dest_id, date, time):
    params = {
        "accessId": ACCESS_ID,
        "origin": origin_id,
        "destination": dest_id,
        "date": date,
        "time": time,
        "format": "json",
        "excludeMeans": "4,5,6,7,8"
    }
    response = requests.get(BASE_URL + "trip", params=params)
    return response.json()

if __name__ == "__main__":
    from_loc = "Wien Westbahnhof"
    to_loc = "Glossystraße 15, 1140 Wien"
    date = "2025-02-24"
    time = "16:23"

    origin_id = resolve_location(from_loc)
    dest_id = resolve_location(to_loc)
    trip = get_trip(origin_id, dest_id, date, time)

    print(json.dumps(trip, indent=2, ensure_ascii=False))
