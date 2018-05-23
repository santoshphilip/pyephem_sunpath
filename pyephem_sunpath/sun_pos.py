from pyephem_sunpath.sunpath import sunposUTC
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