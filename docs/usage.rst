=====
Usage
=====

To use pyephem_sunpath in a project::

    from pyephem_sunpath.sunpath import sunpos
    from datetime import datetime

    thetime = datetime(2018, 5, 23, 13)
    lat = 28.6
    lon = 77.2
    tz = 5.5

    alt, azm = sunpos(thetime, lat, lon, tz, dst=False)
    print(alt, azm)
    
    >> 77.5362391561 232.336370505
