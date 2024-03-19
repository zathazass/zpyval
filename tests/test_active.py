import unittest
import pytest

from zpyval.value import Active


class TestActiveShould(unittest.TestCase):
    def test_on_1_True_true_act_as_True(self):
        assert Active(1).value is True
        assert Active('on').value is True
        assert Active('true').value is True
        assert Active(True).value is True

    def test_off_0_False_false_act_as_False(self):
        assert Active(0).value is False
        assert Active('off').value is False
        assert Active('false').value is False
        assert Active(False).value is False

    def test_not_null(self):
        pytest.raises(ValueError, Active, None)

    def test_not_blank(self):
        pytest.raises(ValueError, Active, '')

    def test_invalid_option_raises_ValueError(self):
        pytest.raises(ValueError, Active, 'tru')
        pytest.raises(ValueError, Active, 'T')