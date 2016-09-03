import urllib3

REQUEST_TYPE = 'GET'
REQUEST_URL = 'http://api.sunrise-sunset.org/json'
CHARACTER_OFFSET = 2
ENCODING = "utf-8"
BEGINNING_INDEX = ':'
ENDING_INDEX = "}"
DATA_SPLIT = ","
DATE = "today"


class FetchSunTimes:
    def __init__(self, lat, lon):
        """
        Populates and parses location data in Location object
        """

        url = REQUEST_URL + "?lat=" + lat + "&lng=" + lon + "&date=" + DATE
        http = urllib3.PoolManager()
        r = http.request(REQUEST_TYPE, url)

        self.__RAW_SUN_DATA__ = sun_json_parse(r.data)
        self.__SUN_DATA__ = self.__RAW_SUN_DATA__.split(DATA_SPLIT)

        self.SUNRISE = self.__SUN_DATA__[0]
        self.SUNSET = self.__SUN_DATA__[1]
        self.SOLAR_NOON = self.__SUN_DATA__[2]
        self.DAY_LENGTH = self.__SUN_DATA__[3]
        self.CIVIL_TWILIGHT_BEGIN = self.__SUN_DATA__[4]
        self.CIVIL_TWILIGHT_END = self.__SUN_DATA__[5]
        self.NAUTICAL_TWILIGHT_BEGIN = self.__SUN_DATA__[6]
        self.NAUTICAL_TWILIGHT_END = self.__SUN_DATA__[7]
        self.ASTROLOGICAL_TWILIGHT_BEGIN = self.__SUN_DATA__[8]
        self.ASTROLOGICAL_TWILIGHT_END = self.__SUN_DATA__[9]


def sun_json_parse(byte_array):
    """
    Processes byte array received from get request containing locational data
    :param byte_array: data returned from URL get request
    :return: string containing raw lat lon
    """
    string = byte_array.decode(ENCODING)
    location_begin = string.index(BEGINNING_INDEX) + CHARACTER_OFFSET
    location_end = string[location_begin:].index(ENDING_INDEX)
    return string[location_begin:location_begin + location_end]

# if __name__ = "__main__":
    #Prompt user for date

    #Prompt user for lat & lon


    # instance = FetchSunTimes()
    # for i in range (0, 10):
    #     print(instance.__SUN_DATA__[i])
