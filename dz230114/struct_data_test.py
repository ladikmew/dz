from unittest import TestCase
from struct_data import DoubleLinkedList
from struct_data import ArrayList
from struct_data import Queue
from struct_data import Stack
import unittest


class TestDoubleLinkedList(TestCase):

    def test_append(self):
        self.a = DoubleLinkedList()
        l = self.a.len
        self.a.append(5)
        self.assertEqual(self.a.len, l + 1)
        self.assertEqual(self.a.geti(self.a.finish), 5)

    def test_len(self):
        self.a = DoubleLinkedList()
        for i in range(10):
            self.a.append(i)
        self.assertEqual(self.a.len, 10)

    def test_len2(self):
        self.a = DoubleLinkedList()
        for i in range(10):
            self.a.append(i)
        for j in range(5):
            self.a.remove(self.a.finish)
        self.assertEqual(self.a.len, 5)

    def test_insert(self):
        self.a = DoubleLinkedList()
        for el in [1, 2, 3, 4]:
            self.a.append(el)
        ind = self.a.search(0)
        self.a.insert(ind, 5)
        self.assertEqual(self.a.geti(self.a.start), 5)

    def test_search(self):
        self.a = DoubleLinkedList()
        for el in [1, 2, 3, 4]:
            self.a.append(el)
        k = self.a.search(0)
        self.assertEqual(self.a.geti(k), 1)

    def test_search2(self):
        self.a = DoubleLinkedList()
        for el in [1, 2, 3, 4]:
            self.a.append(el)
        for el in range(2):
            self.a.remove(self.a.finish)
        for el in [5, 6, 7, 8]:
            self.a.append(el)
        k = self.a.search(3)
        self.assertEqual(self.a.geti(k), 6)

    def test_geti(self):
        self.a = DoubleLinkedList()
        self.a.append(1)
        h = self.a.geti(self.a.start)
        self.assertEqual(h, 1)


class TestArrayList(TestCase):
    def test_append(self):
        self.a = ArrayList()
        l = self.a.len()
        self.a.append(1)
        self.assertEqual(self.a.len(), l + 1)

    def test_len(self):
        self.a = ArrayList()
        r = self.a.len()
        self.assertEqual(self.a.len(), r)

    def test_seti(self):
        self.a = ArrayList()
        self.a.append(1)
        self.a.append(3)
        self.a.seti(1, 5)
        self.assertEqual(self.a.len(), 2)


class TestQueue(TestCase):
    def test_pop(self):
        self.a = Queue()
        self.a.push(1)
        self.a.push(2)
        r = self.a.pop()
        self.assertEqual(r, 1)

    def test_push(self):
        self.a = Queue()
        l = self.a.len()
        self.a.push(1)
        self.assertEqual(self.a.len(), l + 1)

    def test_top(self):
        self.a = Queue()
        self.a.push(1)
        self.a.push(2)
        s = self.a.top()
        self.assertEqual(s, 1)

    def test_len(self):
        self.a = Queue()
        r = self.a.len()
        self.assertEqual(self.a.len(), r)


class TestStack(TestCase):
    def test_pop(self):
        self.a = Stack()
        self.a.push(1)
        self.a.push(2)
        f = self.a.pop()
        self.assertEqual(f,2)

    def test_len(self):
        self.a = Stack()
        r = self.a.len()
        self.assertEqual(self.a.len(), r)

    def test_push(self):
        self.a = Stack()
        l = self.a.len()
        self.a.push(1)
        self.assertEqual(self.a.len(), l + 1)

    def test_top(self):
        self.a = Stack()
        self.a.push(1)
        self.a.push(2)
        self.a.push(3)
        self.assertEqual(self.a.top(), 3)


if __name__ == "__main__":
    unittest.main()
