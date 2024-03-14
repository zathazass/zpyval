import pytest
import unittest

from zpyval.value import Value

class TestValueShould(unittest.TestCase):
    def setUp(self):
        self.value = 1
        self.value_obj = Value(self.value)

    def test_get_single_value_and_store_it_in_value(self):
        assert self.value_obj.value == self.value

    def test_raise_error_when_set_value(self):
        with pytest.raises(AttributeError):
            self.value_obj.value = 4

    def test_call_method_returns_value(self):
        assert self.value_obj() == self.value

    def test_str_of_value_obj_returns_str_value(self):
        assert str(self.value_obj) == str(self.value)

    def test_repr_of_value_obj_returns_repr_value(self):
        assert repr(self.value_obj) == str(self.value)