from unittest import TestCase


from utils import duplaz


def test_duplaz():
    assert duplaz(8) == 16
    assert duplaz(7) == 14
    assert duplaz(0) == 0
    assert duplaz(-1) == -2
    assert duplaz(-5) == -10


class Test(TestCase):
    def test_duplaz(self):
        assert duplaz(8) == 16
        assert duplaz(7) == 14
        assert duplaz(-5) == -10
        assert duplaz(0) == 0
