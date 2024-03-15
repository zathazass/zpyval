import unittest
import pytest

from zpyval.value import Username


class TestUsernameShould(unittest.TestCase):
    def test_null_username_raises_ValueError(self):
        pytest.raises(ValueError, Username, None)

    def test_instance_of_str(self):
        pytest.raises(ValueError, Username, 1)

    def test_blank_username_raises_ValueError(self):
        pytest.raises(ValueError, Username, '')

    def test_username_does_not_allow_invalid_chars(self):
        pytest.raises(ValueError, Username, 'zatha.123')
        pytest.raises(ValueError, Username, '@zatha123')
        pytest.raises(ValueError, Username, 'zatha 1')

    def test_username_accepts_proper_value(self):
        value = 'Zass@1'
        assert Username(value).value == value