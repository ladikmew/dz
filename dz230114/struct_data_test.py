from unittest import TestCase
from struct_data import DoubleLinkedList
from struct_data import ArrayList
from struct_data import Queue
from struct_data import Stack


class TestDoubleLinkedList(TestCase):

    def test_append(self):
        self.a = DoubleLinkedList()
        l = self.a.len()
        self.a.append(5)
        self.assertEqual(self.a.len(), l + 1)

    def test_len(self):
        self.a = DoubleLinkedList()
        r = len(self.a)
        self.assertEqual(self.a.len(), r)

    def test_insert(self):
        self.a = [1, 2, 3, 4]
        # self.a.append(1)
        self.a.insert(0, 5)
        l = [5, 1, 2, 3, 4]
        self.assertEqual(self.a, l)

    def test_search(self):
        self.a = DoubleLinkedList()
        self.a.append(1)
        self.a.search(0)
        l = self.a[0]
        self.assertEqual(self.a, l)

    def test_geti(self):
        self.a = DoubleLinkedList()
        self.a.append(1)
        self.a.geti(0)
        l = self.a[0]
        self.assertEqual(self.a, l)


class TestArrayList(TestCase):
    def test_append(self):
        self.a = ArrayList()
        l = self.a.len()
        self.a.append(1)
        self.assertEqual(self.a.len(), l + 1)

    def test_len(self):
        self.a = ArrayList()
        r = len(self.a)
        self.assertEqual(self.a.len(), r)

    def test_geti(self):
        self.a = ArrayList()
        self.a.append(1)
        self.a.geti(0)
        l = self.a[0]
        self.assertEqual(self.a, l)

    def test_seti(self):
        self.a = [1, 2, 3, 4]
        self.a.seti(1, 5)
        l = [1, 5, 3, 4]
        self.assertEqual(self.a, l)


class TestQueue(TestCase):

    def pop(self):
        self.a = Queue()
        l = self.a.len()
        self.a.pop()
        self.assertEqual(self.a.len(), l - 1)

    def push(self):
        self.a = Queue()
        l = self.a.len()
        self.a.push(1)
        self.assertEqual(self.a.len(), l + 1)

    def top(self):
        self.a = Queue()
        r = self.a[len(self.a) - 1]
        self.a.top()
        self.assertEqual(self.a, r)

    def len(self):
        self.a = Queue()
        r = len(self.a)
        self.assertEqual(self.a.len(), r)


class TestStack(TestCase):
    def pop(self):
        self.a = Stack()
        l = self.a.len()
        self.a.pop()
        self.assertEqual(self.a.len(), l - 1)

    def len(self):
        self.a = Stack()
        r = len(self.a)
        self.assertEqual(self.a.len(), r)

    def push(self):
        self.a = Stack()
        l = self.a.len()
        self.a.push(1)
        self.assertEqual(self.a.len(), l + 1)

    def top(self):
        self.a = Stack()
        r = self.a[len(self.a) - 1]
        self.a.top()
        self.assertEqual(self.a, r)
