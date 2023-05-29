from unittest import TestCase
from 112601_1 import fibonachi

class Test(TestCase):
    def test_fibonachi_1(self):
        a = 233
        b = fibonachi(a)
        self.assertEqual(13,b)
    def test_fibonachi_2(self):
        a = 46368
        b = fibonachi(a)
        self.assertEqual(24,b)
    def test_fibonachi_3(self):
        a = 1000000
        b = fibonachi(a)
        self.assertEqual(-1,b)

    def test_fibonachi_4(self):
        a = 2584
        b = fibonachi(a)
        self.assertEqual(18,b)


