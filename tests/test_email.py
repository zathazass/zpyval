import unittest
import pytest

from zpyval.value import Email


class TestEmailShould(unittest.TestCase):
    def test_isinstance_of_str(self):
        pytest.raises(ValueError, Email, 1)

    def test_not_blank(self):
        pytest.raises(ValueError, Email, '')

    def test_matches_pattern(self):
        assert Email('a3@gm.com').value == 'a3@gm.com'
        assert Email('a+@2gm.com').value == 'a+@2gm.com'
        assert Email('_a@gm.com').value == '_a@gm.com'
        assert Email('a.sa@w-gmail.com').value == 'a.sa@w-gmail.com'

    def test_invalid_formats(self):
        pytest.raises(ValueError, Email, '2@gmail.com')
        pytest.raises(ValueError, Email, 'a@-gmail.com')
        pytest.raises(ValueError, Email, 'a@g.c')
        pytest.raises(ValueError, Email, 'a@gmail.c.com')
        pytest.raises(ValueError, Email, 'a@g-.c0')
        pytest.raises(ValueError, Email, 'a@g-g-.com')
        pytest.raises(ValueError, Email, 'a@g--g.com')

    def test_work_email(self):
        assert Email('a@stech.com').is_work() is True

    def test_public_email(self):
        assert Email('a@gmail.com').is_public() is True
        assert Email('a@outlook.com').is_public() is True
        assert Email('a@yahoo.com').is_public() is True
        assert Email('a@rediff.com').is_public() is True

    def test_domain(self):
        assert Email('a@gmail.com').domain() == 'gmail'
        assert Email('a@g-mail.com').domain() == 'g-mail'

    def test_tld(self):
        assert Email('a.b.c@gmail.com').tld() == 'com'