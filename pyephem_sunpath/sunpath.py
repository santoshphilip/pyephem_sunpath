"""Calculate sun path and sun position using pyephen"""

import ephem
import math


# from
# http://rhodesmill.org/pyephem/tutorial.html#computations-for-particular-observers
def sunposUTC(lon, lat, timeUTC):
    """Calculate sun position

    Calculate sun position (altitude, azimuth) for a particular location (longitude, latitude) for a specific date and time (time is in UTC)

    Parameters
    ----------
    lon : str
        longitude in decimals as a string - '-84.39733' West is -ve
    lat : str
        latitude in decimals as a string - '33.775867' North is +ve
    timeUTC: str
        date and time in the format '1984/5/30 16:22:56'. Time is **not** local time, but in UTC

    Returns
    -------
    (float, float)
        Sun position as (altitude, azimuth)
        where altitude and azimuth in degrees - (70.14421911552256, 122.1906772325591)

    """  # noqa: E501
    gatech = ephem.Observer()
    # print '-' * 15
    # print gatech.temp, "Deg C"
    # print gatech.pressure, "mBar"
    # print '-' * 15
    gatech.lon, gatech.lat = lon, lat
    gatech.date = timeUTC
    sun = ephem.Sun()
    sun.compute(gatech)
    # print("%s %s" % (sun.alt, sun.az))
    # # 70:08:39.2 122:11:26.4
    # slight mismatch iwth NOAA web site
    # https://www.esrl.noaa.gov/gmd/grad/solcalc/azel.html
    # 70.22, 122.1
    # May be due to time zone
    return math.degrees(sun.alt), math.degrees(sun.az)

# Sample of documentation
#
#     """Summary line of func.
#
#     Extended description of function. This is a Sample
#     Function to show how the function documentation should be done.
#     This is the numpy style documentation,
#     will be formatted beautifully by sphinx-napoleon extension
#
#     Parameters
#     ----------
#     arg1 : int
#         Description of arg1
#     arg2 : str
#         Description of arg2
#
#     Returns
#     -------
#     bool
#         Description of return value
#
#     """
