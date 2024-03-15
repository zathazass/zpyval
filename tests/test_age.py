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

    def test_age_is_teenage(self):
        assert Age(10).is_teenage() is False
        assert Age(11).is_teenage() is True
        assert Age(19).is_teenage() is True

    def test_is_adult(self):
        assert Age(10).is_adult() is False
        assert Age(18).is_adult() is False
        assert Age(56).is_adult() is True

        