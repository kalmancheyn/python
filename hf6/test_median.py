from unittest import TestCase
from median import isMedian


class Test(TestCase):
    def test_is_median(self):
        assert isMedian([1, 2, 3, 4, 5]) == 3
        assert isMedian([3, 1, 2, 5, 3]) == 3
        assert isMedian([1, 300, 2, 200, 1]) == 2
        assert isMedian([3, 6, 20, 99, 10, 15]) == 12.5