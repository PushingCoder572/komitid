import requests
import json
from datetime import date, datetime, timedelta
from geopy import Nominatim


class Trip:
    def __init__(self, info):
        self.info = info
        self.depart_time = info["LegList"]["Leg"][0]["Origin"]["time"].replace(":00", "")
        self.depart_place = info["LegList"]["Leg"][0]["Origin"]["name"]
        self.arrive_time = info["LegList"]["Leg"][-1]["Destination"]["time"].replace(":00", "")
        self.arrive_place = info["LegList"]["Leg"][-1]["Destination"]["name"]
        self.travel_time = self.calc_travel_time()
        self.leg_info = self.get_leg_info()

    def calc_travel_time(self):
        start = datetime.strptime(self.depart_time, "%H:%M")
        stop = datetime.strptime(self.arrive_time, "%H:%M")

        return stop - start

    def get_leg_info(self):
        final = []
        for i in self.info["LegList"]["Leg"]:
            if i["type"] != "WALK":
                final.append({
                    "o_name": i["Origin"]["name"],
                    "o_time": i["Origin"]["time"].replace(":00", ""),
                    "d_name": i["Destination"]["name"],
                    "d_time": i["Destination"]["time"].replace(":00", ""),
                    "line": i["Product"]["line"],
                    "class": i["Product"]["catOutL"]
                             })

        return final


def geolocate(adress):
    locator = Nominatim(user_agent='myGeocoder')
    location = locator.geocode(adress)
    return location.latitude, location.longitude


def has_numbers(input_string):
    return any(char.isdigit() for char in input_string)


def sl_trip(start, dest, dest_time, dest_date_offset=1):
    today = date.today()
    tomorrow = today + timedelta(days=dest_date_offset)

    d1 = tomorrow.strftime("%Y-%m-%d")

    search_key = '9af74c05d3464ed3b18fa132c9b41726'
    trip_key = '6828b3e5b4b04737b4311891e825e913'

    station_info = [start, dest]

    for i, search_string in enumerate(station_info):
        get_site_id = 'https://api.sl.se/api2/typeahead.json?key=' + search_key + '&searchstring=' + search_string + '&stationsonly=True&maxresults=1'
        req = requests.get(get_site_id)
        req_json = json.loads(req.text)
        station_info[i] = req_json['ResponseData'][0]

    origin_id = station_info[0]["SiteId"]
    dest_id = station_info[1]["SiteId"]

    # http://api.sl.se/api2/TravelplannerV3_1/trip.json?key=6828b3e5b4b04737b4311891e825e913&originId=1225&destId=9668&Date=2020-09-04&Time=09:00&searchForArrival=1
    get_trip = "http://api.sl.se/api2/TravelplannerV3_1/trip.json?key=" + trip_key + "&originId=" + origin_id + "&destId=" + dest_id + "&Date=" + d1 + "&Time=" + dest_time + "&searchForArrival=1"
    req = requests.get(get_trip)
    req_json = json.loads(req.text)

    return req_json["Trip"]
