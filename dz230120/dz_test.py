from collections import deque
from unittest import TestCase
from dz import unique_numbers, sort_stack


class Test(TestCase):
    def test_unique_numbers1(self):
        a = [1, 2, 3]
        b = unique_numbers(a)
        self.assertEqual(a, b)

    def test_unique_numbers2(self):
        a = [3, 3, 3]
        b = unique_numbers(a)
        self.assertEqual([], b)

    def test_unique_numbers3(self):
        a = [1, 2, 3, 3]
        b = unique_numbers(a)
        self.assertEqual([1, 2], b)


class Test(TestCase):
    def test_sort_stack1(self):
        a = deque([1,2])
        sort_stack(a)
        self.assertEqual([2,1],list(a))

    def test_sort_stack2(self):
        a = deque([6,4,9,1])
        sort_stack(a)
        self.assertEqual([9,6,4,1], list(a))

    def test_sort_stack3(self):
        a = deque([])
        sort_stack(a)
        self.assertEqual([],list(a))

    def test_sort_stack4(self):
        a = deque([2,2,6,5,5])
        sort_stack(a)
        self.assertEqual([6,5,5,2,2],list(a))

    def test_sort_stack5(self):
        a = deque([-1,6,-8])
        sort_stack(a)
        self.assertEqual([6,-1,-8],list(a))
