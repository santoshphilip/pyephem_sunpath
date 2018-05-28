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
from pytest_helpers import _almostequal


def test_sunpos_utc():
    """py.test for sunpos_utc"""
    data = (
        ('-84.39733', '33.775867',
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
