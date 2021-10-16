from unittest import TestCase
from digitsum import sumOfDigits


class Test(TestCase):
    def test_sum_of_digits(self):
        assert sumOfDigits(2 ** 15) == 26
        assert sumOfDigits(2 ** 1000) == 1366
