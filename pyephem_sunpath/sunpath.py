"""Calculate sun path and sun position using pyephen"""

import ephem
import math


def sunposUTC(lon, lat, timeUTC):
    """Calculate sun position

    Calculate sun position (altitude, azimuth) for a particular location (longitude, latitude) for a specific date and time (time is in UTC)

    Parameters
    ----------
    lon : str
        longitude in decimals as a string - '-84.39733'
    lat : str
        latitude in decimals as a string - '33.775867'
    timeUTC: str
        date and time in the format '1984/5/30 16:22:56'. Time is **not** local time, but in UTC

    Returns
    -------
    (str, str)
        Sun position as (altitude, azimuth)
        where altitude and azimuth in degrees - (70.14421911552256, 122.1906772325591)

    """
    gatech = ephem.Observer()
    gatech.lon, gatech.lat = lon, lat
    gatech.date = timeUTC
    sun = ephem.Sun()
    sun.compute(gatech)
    print("%s %s" % (sun.alt, sun.az))
    # # 70:08:39.2 122:11:26.4
    # slight mismatch iwth NOAA web site
    # https://www.esrl.noaa.gov/gmd/grad/solcalc/azel.html
    # 70.22, 122.1
    # May be due to time zone
    return math.degrees(sun.alt), math.degrees(sun.az)


# from
# http://rhodesmill.org/pyephem/tutorial.html#computations-for-particular-observers"""
#
#
# import ephem
# import datetime
#
# gatech = ephem.Observer()
# gatech.lon, gatech.lat = '-84.39733', '33.775867'
#
# gatech.date = '1984/5/30 16:22:56'   # 12:22:56 EDT
# # from https://www.upi.com/Archives/1984/05/30/The-moon-obscured-the-sun-today-in-nearly-total/3084617374750/
# # eclipse was at 12:23 p.m
# # gatech.date is in UTC.
# sun, moon = ephem.Sun(), ephem.Moon()
# sun.compute(gatech)
# moon.compute(gatech)
# print("%s %s" % (sun.alt, sun.az))
# # 70:08:39.2 122:11:26.4
# print("%s %s" % (moon.alt, moon.az))
# # 70:08:39.5 122:11:26.0
#
# gatech.date = '1984/5/31 00:00'   # 20:00 EDT
# sun.compute(gatech)
# for i in range(8):
#     old_az, old_alt = sun.az, sun.alt
#     gatech.date += ephem.minute * 5.
#     sun.compute(gatech)
#     sep = ephem.separation((old_az, old_alt), (sun.az, sun.alt))
#     print("%s %s %s" % (gatech.date, sun.alt, sep))


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
