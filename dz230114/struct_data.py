import numpy as np


class ArrayList:
    """
    """

    def __init__(self):
        self.max_len = 8  # сколько мы выделли в памяти
        self.memory_addr = np.zeros((self.max_len,), dtype=np.uint16)  # [0] * self.max_len
        self.memory_obj = []  # не чистите никогда за время работы
        self.len = 0  # какой объем массива заполнен (по сути длина массива)

    def len(self):  # возвращает длину массива
        """
        """
        return self.len

    def seti(self, i, value):  # заменяем элемент по индексу, в место того котрый там был
        if i >= self.len:
            raise IndexError()
        self.memory_obj.append(value)
        self.memory_addr[i] = len(
            self.memory_obj) - 1  # в массиве с ссылками на элементы, элемент входящего индекса заменяем на длину массива значений минус 1

    def geti(self, i):  # возвращает элемент по индексу
        if i >= self.len:
            raise IndexError()
        return self.memory_obj[self.memory_addr[i]]

    def append(self, value):  # добавление элемента в конец
        self.len += 1
        if self.len >= self.max_len // 2:
            # копирование
            self.max_len *= 2
            self.memory_addr2 = np.zeros((self.max_len,),
                                         dtype=np.uint16)  # заполняем массив, с конкретным типом данных, нулями
            self.memory_addr2[:self.max_len // 4] = self.memory_addr[:self.max_len // 4]
            self.memory_addr = self.memory_addr2
        self.seti(self.len - 1, value)


class Node:
    def __init__(self, link_value, link_next, link_prev):  # ссылки на элемнты
        self.link_value = link_value
        self.link_next = link_next
        self.link_prev = link_prev


class DoubleLinkedList:
    def __init__(self):
        self.memory_addr = []  # [0] * self.max_len
        self.memory_obj = []  # не чистите никогда за время работы
        self.len = 0  # какой объем массива заполнен (по сути длина массива)
        self.start = 0
        self.finish = 0

    def append(self, value):
        self.len += 1  # увеличили длину, так как добавили элемент
        self.memory_obj.append(value)
        # if self.start is None:
        #     self.start = 0
        # if self.finish is None:
        #     self.finish = 0

        if self.len == 1:
            self.start = len(self.memory_addr)
            self.finish = len(self.memory_addr)
        node = Node(len(self.memory_obj) - 1, self.start, self.finish)
        self.memory_addr.append(node)

        if self.len > 1:
            self.memory_addr[self.finish].link_next = len(self.memory_addr) - 1  #
        self.finish = len(self.memory_addr) - 1

        self.memory_addr[0].link_prev = self.finish

    def remove(self, link_el):  # удаление элемента из листа
        if self.len > 1:
            node_prev = self.memory_addr[link_el].link_prev
            node_next = self.memory_addr[link_el].link_next

            self.memory_addr[node_prev].link_next = node_next
            self.memory_addr[node_next].link_prev = node_prev

            if link_el == self.start:  # заменяем первый элемент, если удаляем первый элемент
                self.start = node_next
            if link_el == self.finish:
                self.finish = node_prev  # заменяем последний элемент, если удаляем последний элемент
        else:  # если длина листа меньше единички, то сбрасываем начальный и конечный элементы
            self.start = 0
            self.finish = 0

        self.len -= 1  # уменьшили длину, так как удалили элемент

    def insert(self, link_el, value): # вставляет элемент на входящий индекс
        if self.len > 0:
            node_next = self.memory_addr[link_el].link_next
            node_prev = link_el
            self.memory_obj.append(value)
            node = Node(len(self.memory_obj) - 1, node_next, node_prev)
            self.memory_addr.append(node)
            self.memory_addr[link_el].link_next = len(self.memory_addr) - 1

            if link_el == self.finish:
                self.finish = len(self.memory_addr) - 1
        else:
            raise IndexError()

        self.len += 1

    def search(self, index):  # поиск элемента по индексу
        if index >= self.len:
            raise IndexError()
        link_now = self.start  # начинаем с первого элемента искать
        while link_now != self.finish and index > 0:  # ищем пока не последний элемент и уменьшаем индекс на 1
            link_now = self.memory_addr[link_now].link_next
            index -= 1
        if index == 0:
            return link_now
        raise IndexError()

    def geti(self, i):  # возвращает элемент по индексу
        return self.memory_obj[self.memory_addr[i].link_value]


class Stack:
    def __init__(self):
        self.stack = DoubleLinkedList()

    def push(self, value):  # добавление элемента в стек
        self.len += 1
        self.stack.append(value)
        self.start = self.memory_addr[0].link_next

    def pop(self):  # удаление первого элемента из стека
        self.len -= 1
        self.stack.remove(self.stack.start)
        self.start = self.memory_addr[0].link_next

    def top(self):  # возвращает адрес последнего элемента

        return self.stack.finish

    def len(self):  # возвращает длину стека
        return self.stack.len


class Queue:

    def __init__(self):
        self.queue = DoubleLinkedList()

    def push(self, value):  # добавление элемента в конец очереди
        self.len += 1
        self.queue.append(value)
        self.finish = self.memory_addr[value].link_prev


    def pop(self):  # удаление первого элемента из очереди
        self.len -= 1
        self.queue.remove(self.queue.start)
        self.start = self.memory_addr[0].link_next

    def top(self):  # возвращает адрес последнего элемента

        return self.queue.finish

    def len(self):  # возвращает длину очереди
        return self.queue.len
