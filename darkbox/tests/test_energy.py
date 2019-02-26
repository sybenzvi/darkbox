from darkbox import energy

import numpy as np
from numpy.testing import assert_equal

def test_square():
    y = energy.square(np.array([1,2,3]))
    assert_equal(y, 14)
