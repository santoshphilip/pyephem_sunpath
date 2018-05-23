    # from pyephem_sunpath.sunpath
from sunpath import sunposUTC
import math
import datetime


def calc_xyz(alt,az):
    x = math.sin((az-180)*math.pi/180)
    y = math.cos((az-180)*math.pi/180)
    z = math.tan(alt*math.pi/180)
    l = (x**2+y**2+z**2)**.5
    return (x/l,y/l,z/l)


def sun_pos(timestep,lat,lon,mer,xyz=True,year=2018,dst=False):
    """"""
    tz = mer/15.
    if dst:
        tz += 1
    dt = datetime.datetime(year,*timestep) + datetime.timedelta(hours=tz)
    timeUTC = dt.strftime('%Y/%m/%d %H:%M:%S')
    alt,azm = sunposUTC(str(-lon),str(lat),timeUTC)
    azm = azm - 180
    if xyz:
        return calc_xyz(alt,azm)
    else:
        return alt,azm

# Denver Colorado from https://www.esrl.noaa.gov/gmd/grad/solcalc/azel.html
timestep = (5, 23, 13)
lat = 40.125
lon = 105.23694444444445
mer = 7 * 15

alt, azm =  sun_pos(timestep, lat, lon, mer, xyz=False)
print azm, alt
# 38.9440224487 66.4587993035
print 180. + azm, alt
# 218.944022449 66.4587993035
# from https://www.esrl.noaa.gov/gmd/grad/solcalc/azel.html
# 218.93 66.46
# has a slight mismatch. Accuracy is OK for Stephan's purposes.

# from https://www.esrl.noaa.gov/gmd/grad/solcalc/
timestep = (5, 23, 15, 49, 24)
lat = 39.833
lon = 98.583
mer = 6 * 15

alt, azm =  sun_pos(timestep, lat, lon, mer, xyz=False)
print azm, alt
# 80.6560833326 43.8225073752
print 180. + azm, alt
# 260.656083333 43.8225073752
# from https://www.esrl.noaa.gov/gmd/grad/solcalc/
# 260.65 43.83
