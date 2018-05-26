from __future__ import print_function

from sunpath import sunpos_utc
from sunpath import sunpos_radiance
from sunpath import sunpos_radiancexyz
from sunpath import sunpos
import math
import datetime


def calc_xyz(alt, az):
    """calculate the direction vector for the alt, azm"""
    # az = 180. + az
    x_val = math.sin((az - 180) * math.pi / 180)
    y_val = math.cos((az - 180) * math.pi / 180)
    z_val = math.tan(alt * math.pi / 180)
    length = (x_val ** 2 + y_val ** 2 + z_val ** 2) ** .5
    return (x_val / length,  y_val / length, z_val / length)


def sunpos_orig(timestep, lat, lon, mer, xyz=True, year=2018, dst=False):
    """Calculate sun position for Radiance inputs"""
    tz = mer / 15.
    if dst:
        tz += 1
    dt = datetime.datetime(year, * timestep) + datetime.timedelta(hours=tz)
    timeUTC = dt.strftime('%Y/%m/%d %H:%M:%S')
    alt, azm = sunpos_utc(str(-lon), str(lat), timeUTC)
    azm = azm - 180
    if xyz:
        return calc_xyz(alt, azm)
    else:
        return alt, azm


# Denver Colorado from https://www.esrl.noaa.gov/gmd/grad/solcalc/azel.html
timestep = (5, 23, 13)
lat = 40.125
lon = 105.23694444444445
mer = 7 * 15

alt, azm = sunpos_radiance(timestep, lat, lon, mer, dst=False)
print(azm, alt)
# 38.9440224487 66.4587993035
print(180. + azm, alt)
# 218.944022449 66.4587993035
# from https://www.esrl.noaa.gov/gmd/grad/solcalc/azel.html
# 218.93 66.46
# has a slight mismatch. Accuracy is OK for Stephan's purposes.
xx, yy, zz = sunpos_radiancexyz(timestep, lat, lon, mer, dst=False)
print(alt, azm)
print(xx, yy, zz)
print('-' * 5)

alt, azm = sunpos_radiance(timestep, lat, lon, mer, dst=True)
print(alt, azm)
print('-' * 5)

# from https://www.esrl.noaa.gov/gmd/grad/solcalc/
timestep = (5, 23, 15, 49, 24)
lat = 39.833
lon = 98.583
mer = 6 * 15

alt, azm = sunpos_radiance(timestep, lat, lon, mer, dst=False)
print(azm, alt)
# 80.6560833326 43.8225073752
print(180. + azm, alt)
# 260.656083333 43.8225073752
# from https://www.esrl.noaa.gov/gmd/grad/solcalc/
# 260.65 43.83

xx, yy, zz = sunpos_radiancexyz(timestep, lat, lon, mer, dst=False)
print(alt, azm)
print(xx, yy, zz)
print('-' * 5)

alt, azm = sunpos_radiance(timestep, lat, lon, mer, dst=True)
print(alt, azm)
print('-' * 5)

timestep = (2018, 5, 23, 13)
lat = 40.125
lon = -105.23694444444445
tzone = -7


alt, azm = sunpos(datetime.datetime(*timestep), lat, lon, tzone, dst=False)
print(alt, azm)
alt, azm = sunpos(datetime.datetime(*timestep), lat, lon, tzone, dst=True)
print(alt, azm)
print('-' * 5)

# New Delhi
timestep = (5, 23, 13)
lat = 28.6
lon = -77.2
mer = -5.5 * 15

alt, azm = sunpos_radiance(timestep, lat, lon, mer, dst=False)
print(azm, alt)
# 80.6560833326 43.8225073752
print(180. + azm, alt)

# New Delhi
timestep = (2018, 5, 23, 13)
lat = 28.6
lon = 77.2
tz = 5.5

alt, azm = sunpos(datetime.datetime(*timestep), lat, lon, tz, dst=False)
print(azm, alt)
# 80.6560833326 43.8225073752
# print 180. + azm, alt

# sunpos_utc
# sunpos_radiance
# sunpos(datetime.datetime(*timestep), lat, lon, tz, dst=False)
