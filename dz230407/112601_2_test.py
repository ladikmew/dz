from unittest import TestCase
from 112601_2 import fibonachi


class Test(TestCase):
    def test_fibonachi_1(self):
        a = 1
        b = fibonachi(a)
        self.assertEqual(2, b)

    def test_fibonachi_2(self):
        a = 5
        b = fibonachi(a)
        self.assertEqual(5, b)

    def test_fibonachi_3(self):
        a = 19
        b = fibonachi(a)
        self.assertEqual(-1, b)

    def test_fibonachi_4(self):
        a = 10
        b = fibonachi(a)
        self.assertEqual(-1, b)
