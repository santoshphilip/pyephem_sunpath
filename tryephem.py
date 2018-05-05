"""try the examples in pyephem website
from
http://rhodesmill.org/pyephem/tutorial.html#computations-for-particular-observers"""


import ephem
import datetime

gatech = ephem.Observer()
gatech.lon, gatech.lat = '-84.39733', '33.775867'

gatech.date = '1984/5/30 16:22:56'   # 12:22:56 EDT
# from https://www.upi.com/Archives/1984/05/30/The-moon-obscured-the-sun-today-in-nearly-total/3084617374750/
# eclipse was at 12:23 p.m
sun, moon = ephem.Sun(), ephem.Moon()
sun.compute(gatech)
moon.compute(gatech)
print("%s %s" % (sun.alt, sun.az))
# 70:08:39.2 122:11:26.4
print("%s %s" % (moon.alt, moon.az))
# 70:08:39.5 122:11:26.0

gatech.date = '1984/5/31 00:00'   # 20:00 EDT
sun.compute(gatech)
for i in range(8):
    old_az, old_alt = sun.az, sun.alt
    gatech.date += ephem.minute * 5.
    sun.compute(gatech)
    sep = ephem.separation((old_az, old_alt), (sun.az, sun.alt))
    print("%s %s %s" % (gatech.date, sun.alt, sep))
