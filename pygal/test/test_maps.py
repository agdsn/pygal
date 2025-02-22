# -*- coding: utf-8 -*-
# This file is part of pygal
#
# A python svg graph plotting library
# Copyright © 2012-2016 Kozea
#
# This library is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with pygal. If not, see <http://www.gnu.org/licenses/>.
"""Map plugins tests are imported here"""

from importlib.metadata import entry_points

# Load plugins tests
for entry in entry_points(group="pygal.test.test_maps"):
    module = entry.load()
    for k, v in module.__dict__.items():
        if k.startswith('test_'):
            globals()['test_maps_' + entry.name + '_' + k[5:]] = v
