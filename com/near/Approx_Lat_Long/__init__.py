"""
Copyright (c) 2016 James Warne

James Warne <jwarne90@gmail.com> and located at:
https://github.com/N3ar/LatLong

Licensed under the MIT License

Methods for getting current geographic coordinates (latitude and longitude)
Features:
    Output lat/lon information into a string or list
    lat/lon information is returned in decimal format
Written July 01, 2016
Updated Sept 02, 2016
Author: James Warne
"""
from com.near.Approx_Lat_Long import fetchLatLong


class Location:
    def __init__(self):
        """
        Populates and parses location data in Location object
        """
        location_data = fetchLatLong.FetchLocation()

        self.LATITUDE = location_data.LATITUDE
        self.LONGITUDE = location_data.LONGITUDE

    def set_latitude(self, lat):
        self.LATITUDE = lat

    def set_longitude(self, lng):
        self.LONGITUDE = lng

if __name__ == "__main__":
    inst = Location()
    print("The current approximate latitude is: " + inst.LATITUDE)
    print("The current approximate longitude is: " + inst.LONGITUDE)
