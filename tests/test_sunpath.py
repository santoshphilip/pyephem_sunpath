"""py.test for sunpath functions"""

from pyephem_sunpath import sunpath

def test_sunposUTC():
    """py.test for sunposUTC"""
    data = (
        ('-84.39733', '33.775867',
        '1984/5/30 16:22:56',
        ("70:08:39.2", "122:11:26.4")),
            # lon, lat, timeUTC, expected
    )
    for lon, lat, timeUTC, expected in data:
        result = sunpath.sunposUTC(lon, lat, timeUTC)
        assert result == expected