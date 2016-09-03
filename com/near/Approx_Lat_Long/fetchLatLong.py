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
import urllib3

REQUEST_TYPE = 'GET'
REQUEST_URL = 'http://ipinfo.io/json'
CHARACTER_OFFSET = 7
ENCODING = "utf-8"
BEGINNING_INDEX = 'loc'
ENDING_INDEX = "\""
SPLITTER = ","


class FetchLocation:
    def __init__(self):
        """
        Populates and parses location data in Location object
        """
        http = urllib3.PoolManager()
        r = http.request(REQUEST_TYPE, REQUEST_URL)

        self.__RAW_LAT_LONG__ = loc_json_parse(r.data)
        self.__LAT_LONG__ = self.__RAW_LAT_LONG__.split(SPLITTER)

        self.LATITUDE = self.__LAT_LONG__[0]
        self.LONGITUDE = self.__LAT_LONG__[1]


def loc_json_parse(byte_array):
    """
    Processes byte array received from get request containing locational data
    :param byte_array: data returned from URL get request
    :return: string containing raw lat lon
    """
    string = byte_array.decode(ENCODING)
    location_begin = string.index(BEGINNING_INDEX) + CHARACTER_OFFSET
    location_end = string[location_begin:].index(ENDING_INDEX)
    return string[location_begin:location_begin + location_end]

if __name__ == "__main__":
    inst = FetchLocation()
    print("The current approximate latitude is: " + inst.LATITUDE)
    print("The current approximate longitude is: " + inst.LONGITUDE)
    print(inst.__LAT_LONG__)
