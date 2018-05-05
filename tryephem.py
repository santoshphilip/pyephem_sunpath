"""try the examples in pyephem website
from
http://rhodesmill.org/pyephem/tutorial.html#computations-for-particular-observers"""


import ephem

gatech = ephem.Observer()
gatech.lon, gatech.lat = '-84.39733', '33.775867'

gatech.date = '1984/5/30 16:22:56'   # 12:22:56 EDT
sun, moon = ephem.Sun(), ephem.Moon()
sun.compute(gatech)
moon.compute(gatech)
print("%s %s" % (sun.alt, sun.az))
# 70:08:39.2 122:11:26.4
print("%s %s" % (moon.alt, moon.az))
# 70:08:39.5 122:11:26.0