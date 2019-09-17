#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2019 Adam.Dybbroe

# Author(s):

#   Adam.Dybbroe <a000680@c21529.ad.smhi.se>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
"""

from level1c4pps import make_azidiff_angle

import numpy as np
import sys
if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

SAT_AZ = np.ma.array([[48.0,  56.0, 64.0,  72.0],
                      [80.0,  88.0, 96.0, 104.0],
                      [-80.0,  -88.0, -96.0, -104.0],
                      [-180.0,  -188.0, -196.0, -204.0]], mask=False)
SUN_AZ = np.ma.array([[148.0,  156.0, 164.0,  172.0],
                      [180.0,  188.0, 196.0, 204.0],
                      [180.0,  188.0, 196.0, 204.0],
                      [185.0,  193.0, 201.0, 209.0]], mask=False)

RES = np.ma.array([[100., 100., 100., 100.],
                   [100., 100., 100., 100.],
                   [100.,  84.,  68.,  52.],
                   [5.,  21.,  37.,  53.]],
                  mask=False)


class TestAzimuthDifferenceAngles(unittest.TestCase):
    """Class for testing the derivation of azimuth difference angles."""

    def test_make_azidiff_angle(self):
        """Test calculating the azimuth difference angles"""

        daz = make_azidiff_angle(SAT_AZ, SUN_AZ)
        np.testing.assert_almost_equal(daz, RES)


def suite():
    """Create the test suite for test_atm_correction_ir."""
    loader = unittest.TestLoader()
    mysuite = unittest.TestSuite()
    mysuite.addTest(loader.loadTestsFromTestCase(TestAzimuthDifferenceAngles))

    return mysuite
