# Copyright (c) 2018 Santosh Philip
# Copyright (c) 2018 Stephen Wasilewski
# =======================================================================
# This file is part of pyephem_sunpath.
#
# Pyephem_sunpath is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pyephem_sunpath is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser Public License for more details.
#
# You should have received a copy of the GNU Lesser Public License
# along with pyephem_sunpath.  If not, see <http://www.gnu.org/licenses/>.
# =======================================================================

"""Calculate sun path and sun position using pyephen"""

from __future__ import print_function

import ephem
import math
import datetime


# from
# http://rhodesmill.org/pyephem/tutorial.html#computations-for-particular-observers
def sunpos_utc(lon, lat, timeutc):
    """Calculate sun position with UTC time

    Calculate sun position (altitude, azimuth) for a particular location (longitude, latitude) for a specific date and time (time is in UTC)

    Parameters
    ----------
    lon : str
        longitude in decimals as a string - '-84.39733' West is -ve
    lat : str
        latitude in decimals as a string - '33.775867' North is +ve
    timeutc: str
        date and time in the format '1984/5/30 16:22:56'. Time is **not** local time, but in UTC

    Returns
    -------
    (float, float)
        Sun position as (altitude, azimuth)
        where altitude and azimuth in degrees - (70.14421911552256, 122.1906772325591)

    """  # noqa: E501
    gatech = ephem.Observer()
    gatech.lon, gatech.lat = lon, lat
    gatech.date = timeutc
    sun = ephem.Sun()
    sun.compute(gatech)
    return math.degrees(sun.alt), math.degrees(sun.az)


def _calc_xyz(alt, az):
    """calculate the direction vector for the alt, azm"""
    # az = 180. + az
    x_val = math.sin((az - 180) * math.pi / 180)
    y_val = math.cos((az - 180) * math.pi / 180)
    z_val = math.tan(alt * math.pi / 180)
    length = (x_val ** 2 + y_val ** 2 + z_val ** 2) ** .5
    return (x_val / length,  y_val / length, z_val / length)


def sunpos_radiance(thetime, lat, lon, mer, year=2018, dst=False):
    """Calculate sun position with radiance inputs

    Calculate sun position (altitude, azimuth) for a particular location (longitude, latitude) for a specific date and time (time is local time). The inputs are in radiance format, that are different from the standard format. The differences are listed below:

    - thetime -> is a tuple without the year (month, day , hour, minute, second)
    - lon -> West is +ve for longitude
    - mer -> meridian for the time zone (instead of time zone)
    - year -> year can be set here. It is usually not of significance in radiance calculations
    - The azimuth in the results are described below

    Parameters
    ----------
    thetime: tuple
        date and time as a tuple without the year. Example: '1984/5/30 16:22:56' would be input as a tuple (5, 30, 16, 22, 56). Note that year is dropped. Time is local time
    lon : float
        longitude in decimals. West is +ve
    lat : float
        latitude in decimals. North is +ve
    mer: float
        Meridian of the time zone. West is +ve
    year: int
        The default year is 2018. this value is not of significant when doing radiance calculations.
    dst: Boolean
        dst=True means **thetime** is daylight savings time

    Returns
    -------
    (float, float)
        Sun position as (altitude, azimuth) where:

        - altitude and azimuth are in degrees.
        - South is 0 degrees azimuth.
        - Azimuth is +ve going west (clockwise) and -ve going east (counter clockwise)
        - if the sun is below the horizon, the altitude will be -ve
        - example (70.14421911552256, 50.1906772325591)
    """  # noqa: E501
    tz = mer / 15.
    if dst:
        tz -= 1
    dt = datetime.datetime(year, * thetime) + datetime.timedelta(hours=tz)
    timeutc = dt.strftime('%Y/%m/%d %H:%M:%S')
    alt, azm = sunpos_utc(str(-lon), str(lat), timeutc)
    azm = azm - 180
    return alt, azm


def sunpos_radiancexyz(thetime, lat, lon, mer, year=2018, dst=False):
    """Calculate sun position with radiance inputs. It returns the x, y, z of a unit vector pointing from the location to the sun

    Calculate sun position (altitude, azimuth) for a particular location (longitude, latitude) for a specific date and time (time is local time). The inputs are in radiance format, that are different from the standard format. The differences are listed below:

    - thetime -> is a tuple without the year (month, day , hour, minute, second)
    - lon -> West is +ve for longitude
    - mer -> meridian for the time zone (instead of time zone)
    - year -> year can be set here. It is usually not of significance in radiance calculations

    Parameters
    ----------
    thetime: tuple
        date and time as a tuple without the year. Example: '1984/5/30 16:22:56' would be input as a tuple (5, 30, 16, 22, 56). Note that year is dropped. Time is local time
    lon : float
        longitude in decimals. West is +ve
    lat : float
        latitude in decimals. North is +ve
    mer: float
        Meridian of the time zone. West is +ve
    year: int
        The default year is 2018. this value is not of significant when doing radiance calculations.
    dst: Boolean
        dst=True means **thetime** is daylight savings time

    Returns
    -------
    (float, float, float)
        Sun position as the (x, y, z) of a unit vector pointing from the location to the sun
    """  # noqa: E501
    tz = mer / 15.
    if dst:
        tz -= 1
    dt = datetime.datetime(year, * thetime) + datetime.timedelta(hours=tz)
    timeutc = dt.strftime('%Y/%m/%d %H:%M:%S')
    alt, azm = sunpos_utc(str(-lon), str(lat), timeutc)
    azm = azm - 180
    return _calc_xyz(alt, azm)


def sunpos(thetime, lat, lon, tz, dst=False):
    """Calculate sun position

    Calculate sun position (altitude, azimuth) for a particular location (longitude, latitude) for a specific date and time (time is local time)

    Parameters
    ----------
    thetime: datetime
        date and time in the datetime format. example: '1984/5/30 16:22:56' would be input as datetime.datetime(1984, 5, 30, 16, 22, 56). Time is local time
    lon : float
        longitude in decimals. West is -ve.
    lat : float
        latitude in decimals. North is +ve
    tz: float
        Timezone. West is -ve
    dst: Boolean
        dst=True means **thetime** is daylight savings time

    Returns
    -------
    (float, float)
        Sun position as (altitude, azimuth) where:

        - altitude and azimuth are in degrees.
        - North is 0 degrees azimuth.
        - Azimuth is +ve in the clockwise direction starting from North
        - example (70.14421911552256, 122.1906772325591)
        - if the sun is below the horizon, the altitude will be -ve
    """  # noqa: E501
    if dst:
        tz += 1
    dt = thetime - datetime.timedelta(hours=tz)
    timeutc = dt.strftime('%Y/%m/%d %H:%M:%S')
    alt, azm = sunpos_utc(str(lon), str(lat), timeutc)
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
