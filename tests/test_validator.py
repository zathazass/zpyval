import pytest

from zpyval.validator import instance_of, is_true, not_null


def test_is_instance_of():
    assert instance_of(1, int) is None
    pytest.raises(ValueError, instance_of, value=1, klass=str)


def test_is_true():
    assert is_true(1 > 0, '') is None
    pytest.raises(ValueError, is_true, 1 > 2, 'value should be greateer than 2')


def test_not_null():
    assert not_null(1) == None
    pytest.raises(ValueError, not_null, None)