from unittest import TestCase
from 112601_3 import fibonachi
from 112601_3 import get_fib

class Test(TestCase):
    def test_fibonachi_1(self):
        a = 89
        b = fibonachi(a)
        self.assertEqual(11, b)

    def test_fibonachi_2(self):
        a =  10946
        b = fibonachi(a)
        self.assertEqual(21, b)

    def test_fibonachi_3(self):
        a = 133333
        b = fibonachi(a)
        self.assertEqual(-1, b)

    def test_fibonachi_4(self):
        a = 2584
        b = fibonachi(a)
        self.assertEqual(18, b)

