from com.near import Approx_Lat_Long, solarData
import datetime
import time

# Constants
YEAR = datetime.datetime.utcnow().year
MONTH = datetime.datetime.utcnow().month
DAY = datetime.datetime.utcnow().day
PM_DELTA = datetime.timedelta(hours=12)
AM_DELTA = datetime.timedelta(days=1)
NOW = datetime.datetime.utcnow()

# Variables
waits = list()
delta = list()
utc_times = list()


def get_current_location():
    return Approx_Lat_Long.Location()


# Populate and order solar times
def event_time_list():
    utc_sun = solarData.SunTimes(LAT, LON)
    utc_times.append(utc_sun.__SOLAR_DATA__[8])
    utc_times.append(utc_sun.__SOLAR_DATA__[6])
    utc_times.append(utc_sun.__SOLAR_DATA__[4])
    utc_times.append(utc_sun.__SOLAR_DATA__[0])
    utc_times.append(utc_sun.__SOLAR_DATA__[1])
    utc_times.append(utc_sun.__SOLAR_DATA__[5])
    utc_times.append(utc_sun.__SOLAR_DATA__[7])
    utc_times.append(utc_sun.__SOLAR_DATA__[9])


# Loop through solar times, converting them to date time
def solar_data_to_datetime():
    pm_flag = 0
    pm_flag_2 = 0
    am_flag = 0

    for i in range(0, 8):
        utc_times[i] = utc_times[i].split(" ")
        utc_times[i][0] = datetime.datetime.strptime(utc_times[i][0], '%H:%M:%S')

        if utc_times[i][1] == 'PM':
            pm_flag = 1
        if utc_times[i][1] == 'PM' and utc_times[i][0].hour != 12:
            pm_flag_2 = 1
        if utc_times[i][1] == 'AM' and pm_flag == 1:
            am_flag = 1
            pm_flag_2 = 0

        utc_times[i][0] = datetime.datetime(YEAR, MONTH, DAY,
                                            utc_times[i][0].hour,
                                            utc_times[i][0].minute,
                                            utc_times[i][0].second)
        if am_flag == 1:
            utc_times[i][0] += AM_DELTA
        if pm_flag == 1 and pm_flag_2 == 1:
            utc_times[i][0] += PM_DELTA
        utc_times[i] = utc_times[i][0]


# Get the change in wait times in seconds
def event_wait_times():
    for i in range(0, 8):
        waits.append(utc_times[i] - NOW)
        if i == 0:
            delta.append(waits[i].seconds)
        elif i > 0:
            delta.append(waits[i].seconds - waits[i-1].seconds)

# Main execution
if __name__ == "__main__":
    # Get location constants
    location = get_current_location()
    LAT = location.LATITUDE
    LON = location.LONGITUDE

    # Execute body
    event_time_list()
    solar_data_to_datetime()
    event_wait_times()

    for j in range(0, 8):
        print("running...")
        time.sleep(delta[j])

        # TODO: RASPI Python interaction with servo motor will be here
        print("made it to step: " + str(j))
        # if j < 4
        # turn 25% on
        # else
        # turn 25% off

# CONST = .02083
#
# sun = JulianSunrise.JulianSun()
# rise = sun.get_julian_sunrise()
# sets = sun.get_julian_sunset()
# now = JulianDay.JulianDay().get_julian_day()
#
# print("Brighten: " + str(rise - CONST))
# print("Sunrise:  " + str(rise))
# print("On:       " + str(rise + CONST))
# print("Current:  " + str(now))
# print("Dimming:  " + str(sets - CONST))
# print("Sunset:   " + str(sets))
# print("Off:      " + str(sets + CONST))
#
# .02083 ~ 30 minutes
