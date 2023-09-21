import time
from threading import Thread


class MyThread(Thread):

    def __init__(self, name, k, list):
        """Инициализация потока"""
        Thread.__init__(self)
        self.name = name
        self.k = k
        self.list = list
        self.r = True

    def run(self):

        while self.r:
            time.sleep(1)

    def stop(self):
        self.r = False


def create_threads():
    """Создаем потоки"""
    thread_list = {}
    while True:
        k = input()
        name = k[-1]

        if (name not in thread_list.keys() and k[:5] == "start"):
            thread_list.setdefault(name, MyThread(name, k, thread_list.keys()))
            thread_list.get(name).start() #запуск потока
            print(f"{name} is running")

        elif k[:4] == "stop":
            thread_list.get(name).stop()
            thread_list.pop(name)
            print(f"{name} stopped")

        else:
            for name in thread_list.keys():
                print(f"{name} is running")



if __name__ == "__main__":
    create_threads()
