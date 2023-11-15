from collections import deque


def contador(stop):
    cont = 1
    while cont <= stop:
        yield cont
        cont += 1


def contador_regressivo(start):
    while start >= 1:
        yield start
        start -= 1


class Scheduler:
    def __init__(self):
        self.queue = deque()

    def add_new(self, coro):
        self.queue.append(coro)

    def run(self):
        while self.queue:
            task = self.queue.popleft()
            try:
                result = next(task)
                print(f"{task=}: {result=}")

                self.queue.append(task)
            except StopIteration:
                ...

    def __repr__(self) -> str:
        return "Scheduler(" + str(self.queue) + ")"


s = Scheduler()
print(s)
s.add_new(contador(10))
s.add_new(contador_regressivo(5))
print(s)

"""python -i exemplo_00.py
Scheduler(deque([]))
Scheduler(deque([<generator object contador at 0x104f0c040>, <generator object contador_regressivo at 0x104e48b80>]))
>>> s.queue
deque([<generator object contador at 0x104f0c040>, <generator object contador_regressivo at 0x104e48b80>])
>>> s.queue.append(contador(5))
>>> task = s.queue.popleft()
>>> task
<generator object contador at 0x104f0c040>
>>> print(task)
<generator object contador at 0x104f0c040>
>>> s.queue.append(contador(5))
>>> s.queue
deque([<generator object contador_regressivo at 0x104e48b80>, <generator object contador at 0x104f0df20>, <generator object contador at 0x104f0e810>])
>>> s.queue.append(contador(15))
>>> s.queue
deque([<generator object contador_regressivo at 0x104e48b80>, <generator object contador at 0x104f0df20>, <generator object contador at 0x104f0e810>, <generator object contador at 0x10515c5f0>])
"""
