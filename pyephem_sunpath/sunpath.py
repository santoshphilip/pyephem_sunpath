"""Calculate sun path and sun position using pyephen"""

import ephem
import math
import datetime


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


def calc_xyz(alt, az):
    """calculate the direction vector for the alt, azm"""
    # az = 180. + az
    x_val = math.sin((az - 180) * math.pi / 180)
    y_val = math.cos((az - 180) * math.pi / 180)
    z_val = math.tan(alt * math.pi / 180)
    length = (x_val ** 2 + y_val ** 2 + z_val ** 2) ** .5
    return (x_val / length,  y_val / length, z_val / length)


def sunpos_radiance(thetime, lat, lon, mer, xyz=True, year=2018, dst=False):
    """Calculate sun position for Radiance inputs"""
    tz = mer / 15.
    if dst:
        tz -= 1
    dt = datetime.datetime(year, * thetime) + datetime.timedelta(hours=tz)
    timeUTC = dt.strftime('%Y/%m/%d %H:%M:%S')
    alt, azm = sunposUTC(str(-lon), str(lat), timeUTC)
    azm = azm - 180
    if xyz:
        return calc_xyz(alt, azm)
    else:
        return alt, azm


def sunpos(thetime, lat, lon, tz, dst=False):
    """Calculate sun position for Radiance inputs"""
    if dst:
        tz -= 1
    dt = datetime.datetime(* thetime) + datetime.timedelta(hours=tz)
    timeUTC = dt.strftime('%Y/%m/%d %H:%M:%S')
    alt, azm = sunposUTC(str(lon), str(lat), timeUTC)
    return alt, azm

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
