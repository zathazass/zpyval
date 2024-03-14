import unittest
import pytest

from zpyval.value import Age

class TestAgeShould:
    def test_age_greater_than_zero(self):
        assert Age(1).value == 1
        pytest.raises(ValueError, Age, -1)

    def test_age_within_limit_150(self):
        assert Age(150).value == 150
        pytest.raises(ValueError, Age, 151)