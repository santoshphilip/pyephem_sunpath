"""py.test for sunpath functions"""

from pyephem_sunpath import sunpath
from pyephem_sunpath.pytest_helpers import almostequal


def test_sunposUTC():
    """py.test for sunposUTC"""
    data = (
        ('-84.39733', '33.775867',
         '1984/5/30 16:22:56',
         (70.14421911552256, 122.1906772325591)),
        # lon, lat, timeUTC, expected
    )
    for lon, lat, timeUTC, expected in data:
        result = sunpath.sunposUTC(lon, lat, timeUTC)
        assert result == expected


def test_unitvector_sunpos():
    """py.test for unitvector_sunpos"""
    data = ((43.8225073752, 260.656083333, (-0.711915254482, -0.117140973417, 0.692426647944)), # alt, az, xyz
    )
    for alt, az, xyz in data:
        result = sunpath.unitvector_sunpos(alt, az)
        print result
        print xyz
        for rval, xyzval in zip(result, xyz):
            assert almostequal(rval, xyzval)
