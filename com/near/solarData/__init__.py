from com.near.solarData import fetchSolarData

ENTRY_SPLIT = "\""


class SunTimes:
    def __init__(self, lat, lon):
        """
        Populates and parses location data in Location object
        """

        solar_data = fetchSolarData.FetchSunTimes(lat, lon)

        self.__SOLAR_DATA__ = solar_data.__SUN_DATA__
        for i in range(0, 10):
            self.__SOLAR_DATA__[i] = sun_data_parse(self.__SOLAR_DATA__[i])

        self.SUNRISE = sun_data_parse(solar_data.SUNRISE)
        self.SUNSET = sun_data_parse(solar_data.SUNSET)
        self.SOLAR_NOON = sun_data_parse(solar_data.SOLAR_NOON)
        self.DAY_LENGTH = sun_data_parse(solar_data.DAY_LENGTH)
        self.CIVIL_TWILIGHT_BEGIN = sun_data_parse(solar_data.CIVIL_TWILIGHT_BEGIN)
        self.CIVIL_TWILIGHT_END = sun_data_parse(solar_data.CIVIL_TWILIGHT_END)
        self.NAUTICAL_TWILIGHT_BEGIN = sun_data_parse(solar_data.NAUTICAL_TWILIGHT_BEGIN)
        self.NAUTICAL_TWILIGHT_END = sun_data_parse(solar_data.NAUTICAL_TWILIGHT_END)
        self.ASTROLOGICAL_TWILIGHT_BEGIN = sun_data_parse(solar_data.ASTROLOGICAL_TWILIGHT_BEGIN)
        self.ASTROLOGICAL_TWILIGHT_END = sun_data_parse(solar_data.ASTROLOGICAL_TWILIGHT_END)


def sun_data_parse(dat_string):
    """
    Processes string array
    :param dat_string: individual JSON entries parsed into python strings
    :return: string containing UTC time of value requested
    """
    return dat_string.split(ENTRY_SPLIT)[3]

if __name__ == "__main__":
    instance = SunTimes()
    print("All values are in UTC")
    print(instance.__SOLAR_DATA__)