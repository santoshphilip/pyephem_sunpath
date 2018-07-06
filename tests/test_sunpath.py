# Copyright (c) 2018 Santosh Philip
# =======================================================================
# This file is part of pyephem_sunpath.
#
# Pyephem_sunpath is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pyephem_sunpath is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser Public License for more details.
#
# You should have received a copy of the GNU Lesser Public License
# along with pyephem_sunpath.  If not, see <http://www.gnu.org/licenses/>.
# =======================================================================

"""py.test for sunpath functions"""

from __future__ import print_function

import datetime
from pyephem_sunpath import sunpath
from tests.pytest_helpers import _almostequal


def test_sunpos_utc():
    """py.test for sunpos_utc"""
    data = (
        ('-84.39733', '33.775867',
         '1984/5/30 16:22:56',
         (70.14421911552256, 122.1906772325591)),
        # lon, lat, timeUTC, expected
        (-84.39733, 33.775867,
         '1984/5/30 16:22:56',
         (70.14421911552256, 122.1906772325591)),
        # lon, lat, timeUTC, expected
    )
    for lon, lat, timeUTC, expected in data:
        result = sunpath.sunpos_utc(lon, lat, timeUTC)
        assert result == expected


def test__calc_xyz():
    """py.test for _calc_xyz"""
    data = (
        (43.8225073752, 80.6560833326,
            (-0.711915254482, -0.117140973417, 0.692426647944)),
        # alt, az, xyz
        (66.4587993035, 38.9440224487,
            (-0.251052481263, -0.310644059369, 0.916773101716)),
        # alt, az, xyz
    )
    for alt, az, xyz in data:
        result = sunpath._calc_xyz(alt, az)
        for rval, xyzval in zip(result, xyz):
            assert _almostequal(rval, xyzval)


def test_sunpos_radiance():
    """py.test sunpos_radiance"""
    # test data from https://www.esrl.noaa.gov/gmd/grad/solcalc/
    data = (
        ((5, 23, 13), 40.125, 105.23694444444445, 7 * 15,
            2018, False, (66.4587993035, 38.9440224487),),
        # thetime, lat, lon, mer, year, dst, expected
        ((5, 23, 15, 49, 24), 39.833, 98.583, 6 * 15,
            2018, False, (43.8225073752, 80.6560833326),),
        # thetime, lat, lon, mer, year, dst, expected
        # ---
        # test for dst=True
        ((5, 23, 13), 40.125, 105.23694444444445, 7 * 15,
            2018, True, (70.5494474088, 1.60339191662),),
        # thetime, lat, lon, mer, year, dst, expected
        ((5, 23, 15, 49, 24), 39.833, 98.583, 6 * 15,
            2018, True, (54.8787531507, 67.2963425991),),
        # thetime, lat, lon, mer, year, dst, expected
        ((5, 23, 13), 40.125, 105.23694444444445, 7 * 15,
            2018, False, (66.4587993035, 38.9440224487),),
        # thetime, lat, lon, mer, year, dst, expected
    )
    for thetime, lat, lon, mer, year, dst, expected in data:
        args = (thetime, lat, lon, mer, year, dst)
        result = sunpath.sunpos_radiance(*args)
        for rval, expval in zip(result, expected):
            assert _almostequal(rval, expval)


def test_sunpos_radiancexyz():
    """py.test sunpos_radiancexyz"""
    # test data from https://www.esrl.noaa.gov/gmd/grad/solcalc/
    data = (
        ((5, 23, 13), 40.125, 105.23694444444445, 7 * 15,
            2018, False,
            (-0.251052481263, -0.310644059369, 0.916773101716),),
        # thetime, lat, lon, mer, year, dst, expected
        ((5, 23, 15, 49, 24), 39.833, 98.583, 6 * 15,
            2018, False,
            (-0.711915254482, -0.117140973417, 0.692426647944),),
    )
    for thetime, lat, lon, mer, year, dst, expected in data:
        args = (thetime, lat, lon, mer, year, dst)
        result = sunpath.sunpos_radiancexyz(*args)
        for rval, expval in zip(result, expected):
            assert _almostequal(rval, expval)


def test_sunpos():
    """py.test for sunpos"""
    data = (
        ((2018, 5, 23, 13), 40.125, -105.23694444444445,
            -7, False,
            (66.4587993035, 218.944022449)),
        # thetime, lat, lon, tz, dst, expected
        ((2018, 5, 23, 13), 40.125, -105.23694444444445,
            -7, True,
            (70.5494474088, 181.603391917)),
        # thetime, lat, lon, tz, dst, expected
    )
    for thetime, lat, lon, tz, dst, expected in data:
        thetime = datetime.datetime(*thetime)
        result = sunpath.sunpos(thetime, lat, lon, tz, dst)
        for rval, expval in zip(result, expected):
            assert _almostequal(rval, expval)


def test_sunrise_utc():
    """py.test for sunrise_utc"""
    data = (
        ('33.8', '-84.4', '2009/09/06 17:00', "2009/9/6 11:14:57"),
        # lat, lon, utctime, expected
    )
    for lat, lon, utctime, expected in data:
        result = sunpath.sunrise_utc(lat, lon, utctime)
        assert result == expected


def test_sunset_utc():
    """py.test for sunset_utc"""
    data = (
        ('33.8', '-84.4', '2009/09/06 17:00', "2009/9/6 23:56:10"),
        # lat, lon, utctime, expected
    )
    for lat, lon, utctime, expected in data:
        result = sunpath.sunset_utc(lat, lon, utctime)
        assert result == expected


def test_local2utc():
    """py.test for local2utc"""
    dtime = datetime.datetime
    data = (
            (dtime(2018, 2, 28, 10), -3, False, '2018/02/28 13:00:00'),
            # thetime, tz, dst, expected
            (dtime(2018, 2, 28, 10), -3, True, '2018/02/28 12:00:00'),
            # thetime, tz, dst, expected
            (dtime(2018, 2, 28, 10), 3, False, '2018/02/28 07:00:00'),
            # thetime, tz, dst, expected
            (dtime(2018, 2, 28, 10), 3, True, '2018/02/28 06:00:00'),
            # thetime, tz, dst, expected
    )
    for thetime, tz, dst, expected in data:
        result = sunpath.local2utc(thetime, tz, dst)
        assert result == expected


def testutc2local():
    """py.test for utc2local"""
    dtime = datetime.datetime
    data = (
            (dtime(2018, 2, 28, 10), -3, False, '2018/02/28 13:00:00'),
            # expected, tz, dst, utctime
            (dtime(2018, 2, 28, 10), -3, True, '2018/02/28 12:00:00'),
            # expected, tz, dst, utctime
            (dtime(2018, 2, 28, 10), 3, False, '2018/02/28 07:00:00'),
            # expected, tz, dst, utctime
            (dtime(2018, 2, 28, 10), 3, True, '2018/02/28 06:00:00'),
            # expected, tz, dst, utctime
    )
    for expected, tz, dst, utctime in data:
        result = sunpath.utc2local(utctime, tz, dst)
        assert result == expected


def test_sunrise():
    """py.test for sunrise"""
    dtime = datetime.datetime
    data = (
        (dtime(2009, 9, 6), 33.8, -84.4, -5, True,
            dtime(2009, 9, 6, 7, 14, 57)),
        # thedate, lat, lon, tz, dst, expected
    )
    for thedate, lat, lon, tz, dst, expected in data:
        result = sunpath.sunrise(thedate, lat, lon, tz, dst)
        assert result == expected


def test_sunset():
    """py.test for sunset"""
    dtime = datetime.datetime
    data = (
        (dtime(2009, 9, 6), 33.8, -84.4, -5, True,
            dtime(2009, 9, 6, 7+12, 56, 10)),
        # thedate, lat, lon, tz, dst, expected
    )
    for thedate, lat, lon, tz, dst, expected in data:
        result = sunpath.sunset(thedate, lat, lon, tz, dst)
        assert result == expected
