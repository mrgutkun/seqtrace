# Copyright (C) 2014 Brian J. Stucky
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.



# Sets up a reference to a PairwiseAlignment object.  This will allow client
# code to use PairwiseAlignment without needing to worry about whether or not
# the compiled C extension is available.  If the compiled module is available,
# it will be used automatically; otherwise, the native Python module will be used.

try:
    # Try to load the compiled C module.
    from calign import PairwiseAlignment
except ImportError:
    # If that fails, load the Python module.
    from pyalign import PairwiseAlignment

# This is not implemented in C, and not expected to be: actual alignment is done by MUSCLE executable anyway.
from pyalign import MultipleAlignment
