import ephem
atlanta = ephem.Observer()
atlanta.pressure = 0
atlanta.horizon = '-0:34'
atlanta.lat, atlanta.lon = '33.8', '-84.4'
atlanta.date = '2009/09/06 17:00' # noon EST
print(atlanta.previous_rising(ephem.Sun()))

# 2009/9/6 11:14:57
# 2009/9/5 11:14:16
# 2009/9/6 11:14:57
