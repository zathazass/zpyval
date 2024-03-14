import unittest
import pytest

from zpyval.value import Id


class TestIdShould(unittest.TestCase):
    def test_isinstance_of_int_raises_ValueError(self):
        pytest.raises(ValueError, Id, '3')

    def test_value_greater_than_zero_raises_ValueError(self):
        pytest.raises(ValueError, Id, -1)
        pytest.raises(ValueError, Id, 0)