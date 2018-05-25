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


def test_calc_xyz():
    """py.test for calc_xyz"""
    data = (
        (43.8225073752, 80.6560833326,
            (-0.711915254482, -0.117140973417, 0.692426647944)),
        # alt, az, xyz
        (66.4587993035, 38.9440224487,
            (-0.251052481263, -0.310644059369, 0.916773101716)),
        # alt, az, xyz
    )
    for alt, az, xyz in data:
        result = sunpath.calc_xyz(alt, az)
        print result
        print xyz
        for rval, xyzval in zip(result, xyz):
            assert almostequal(rval, xyzval)


def test_sunpos_radiance():
    """py.test sunpos_radiance"""
    # test data from https://www.esrl.noaa.gov/gmd/grad/solcalc/
    data = (
        ((5, 23, 13), 40.125, 105.23694444444445, 7 * 15,
            False, 2018, False, (66.4587993035, 38.9440224487),),
        # thetime, lat, lon, mer, xyz, year, dst, expected
        ((5, 23, 15, 49, 24), 39.833, 98.583, 6 * 15,
            False, 2018, False, (43.8225073752, 80.6560833326),),
        # thetime, lat, lon, mer, xyz, year, dst, expected
        # ---
        # test for xyz=True
        ((5, 23, 13), 40.125, 105.23694444444445, 7 * 15,
            True, 2018, False,
            (-0.251052481263, -0.310644059369, 0.916773101716),),
        # thetime, lat, lon, mer, xyz, year, dst, expected
        ((5, 23, 15, 49, 24), 39.833, 98.583, 6 * 15,
            True, 2018, False,
            (-0.711915254482, -0.117140973417, 0.692426647944),),
        # thetime, lat, lon, mer, xyz, year, dst, expected
        # ---
        # test for dst=True
        ((5, 23, 13), 40.125, 105.23694444444445, 7 * 15,
            False, 2018, True, (70.5494474088, 1.60339191662),),
        # thetime, lat, lon, mer, xyz, year, dst, expected
        ((5, 23, 15, 49, 24), 39.833, 98.583, 6 * 15,
            False, 2018, True, (54.8787531507, 67.2963425991),),
        # thetime, lat, lon, mer, xyz, year, dst, expected
        ((5, 23, 13), 40.125, 105.23694444444445, 7 * 15,
            False, 2018, False, (66.4587993035, 38.9440224487),),
        # thetime, lat, lon, mer, xyz, year, dst, expected
    )
    for thetime, lat, lon, mer, xyz, year, dst, expected in data:
        args = (thetime, lat, lon, mer, xyz, year, dst)
        result = sunpath.sunpos_radiance(*args)
        for rval, expval in zip(result, expected):
            assert almostequal(rval, expval)


def test_sunpos():
    """py.test for sunpos"""
    data = (
        ((2018, 5, 23, 13), 40.125, -105.23694444444445,
            -7, False,
            (66.4587993035, 218.944022449)),
        # thetime, lat, lon, tz, dst, expected
        ((2018, 5, 23, 13), 40.125, -105.23694444444445,
            7, True,
            (70.5494474088, 181.603391917)),
        # thetime, lat, lon, tz, dst, expected
    )
    for thetime, lat, lon, tz, dst, expected in data:
        result = sunpath.sunpos(thetime, lat, lon, tz, dst)
        for rval, expval in zip(result, expected):
            assert almostequal(rval, expval)
