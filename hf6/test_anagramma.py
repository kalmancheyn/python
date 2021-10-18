from unittest import TestCase
from anagramma import anagramma1, anagramma2


class Test(TestCase):
    def test_anagramma1(self):
        assert anagramma1("listen", "silent") == True
        assert anagramma1("A gentleman", "Elegant man") == True
        assert anagramma1("Clint Eastwood", "Old west action") == True
        assert anagramma1("dormitory", "dirty room") == True
        assert anagramma1("alma", "korte") == False


    def test_anagramma2(self):
        assert anagramma2("listen", "silent") == True
        assert anagramma2("A gentleman", "Elegant man") == True
        assert anagramma2("Clint Eastwood", "Old west action") == True
        assert anagramma2("dormitory", "dirty room") == True
        assert anagramma2("alma", "korte") == False
