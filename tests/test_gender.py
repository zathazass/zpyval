import unittest
import pytest

from zpyval.value import Gender


class TestGenderShould:
    def test_blank_raises_ValueError(self):
        pytest.raises(ValueError, Gender, '')

    def test_allow_null(self):
        assert Gender(None).value == None

    def test_accept_female_and_Female_and_FEMALE_and_F_and_f_returns_female(self):
        assert Gender('F').value == 'female'
        assert Gender('f').value == 'female'
        assert Gender('female').value == 'female'
        assert Gender('Female').value == 'female'
        assert Gender('FEMALE').value == 'female'

    def test_accept_male_and_Male_and_MALE_and_M_and_m_returns_male(self):
        assert Gender('M').value == 'male'
        assert Gender('m').value == 'male'
        assert Gender('male').value == 'male'
        assert Gender('Male').value == 'male'
        assert Gender('MALE').value == 'male'