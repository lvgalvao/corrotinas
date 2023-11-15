from collections import deque
from time import sleep


def contador(name, stop):
    cont = 1
    while cont <= stop:
        yield f"{name}: {cont}"
        cont += 1
        sleep(0.5)


def contador_regressivo(name, start):
    while start >= 1:
        yield f"{name}: {start}"
        start -= 1
        sleep(0.5)


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
s.add_new(contador("RunTime A", 10))
s.add_new(contador_regressivo("RunTime B", 20))
print(s)

from threading import Thread

t = Thread(target=s.run, daemon=True)

"""
(corrotinas-py3.9) ➜  corrotinas git:(main) ✗ python -i exemplo_02.py
Scheduler(deque([]))
Scheduler(deque([<generator object contador at 0x100c64040>, <generator object contador_regressivo at 0x100c640b0>]))
>>> t.start()
task=<generator object contador at 0x100c64040>: result='RunTime A: 1'
task=<generator object contador_regressivo at 0x100c640b0>: result='RunTime B: 20'
>>> task=<generator object contador at 0x100c64040>: result='RunTime A: 2'
task=<generator object contador_regressivo at 0x100c640b0>: result='RunTime B: 19'
task=<generator object contador at 0x100c64040>: result='RunTime A: 3'
s.add_new(contador('RunTime C', 10))
>>> 
>>> task=<generator object contador_regressivo at 0x100c640b0>: result='RunTime B: 18'
task=<generator object contador at 0x100c64040>: result='RunTime A: 4'
task=<generator object contador at 0x100c64660>: result='RunTime C: 1'
task=<generator object contador_regressivo at 0x100c640b0>: result='RunTime B: 17'
task=<generator object contador at 0x100c64040>: result='RunTime A: 5'
task=<generator object contador at 0x100c64660>: result='RunTime C: 2'
task=<generator object contador_regressivo at 0x100c640b0>: result='RunTime B: 16'
task=<generator object contador at 0x100c64040>: result='RunTime A: 6'
task=<generator object contador at 0x100c64660>: result='RunTime C: 3'
task=<generator object contador_regressivo at 0x100c640b0>: result='RunTime B: 15'
task=<generator object contador at 0x100c64040>: result='RunTime A: 7'
task=<generator object contador at 0x100c64660>: result='RunTime C: 4'
task=<generator object contador_regressivo at 0x100c640b0>: result='RunTime B: 14'
task=<generator object contador at 0x100c64040>: result='RunTime A: 8'
task=<generator object contador at 0x100c64660>: result='RunTime C: 5'
task=<generator object contador_regressivo at 0x100c640b0>: result='RunTime B: 13'
task=<generator object contador at 0x100c64040>: result='RunTime A: 9'
task=<generator object contador at 0x100c64660>: result='RunTime C: 6'
task=<generator object contador_regressivo at 0x100c640b0>: result='RunTime B: 12'
task=<generator object contador at 0x100c64040>: result='RunTime A: 10'
task=<generator object contador at 0x100c64660>: result='RunTime C: 7'
task=<generator object contador_regressivo at 0x100c640b0>: result='RunTime B: 11'
task=<generator object contador at 0x100c64660>: result='RunTime C: 8'
task=<generator object contador_regressivo at 0x100c640b0>: result='RunTime B: 10'
task=<generator object contador at 0x100c64660>: result='RunTime C: 9'
task=<generator object contador_regressivo at 0x100c640b0>: result='RunTime B: 9'
task=<generator object contador at 0x100c64660>: result='RunTime C: 10'
task=<generator object contador_regressivo at 0x100c640b0>: result='RunTime B: 8'
task=<generator object contador_regressivo at 0x100c640b0>: result='RunTime B: 7'
task=<generator object contador_regressivo at 0x100c640b0>: result='RunTime B: 6'
task=<generator object contador_regressivo at 0x100c640b0>: result='RunTime B: 5'
task=<generator object contador_regressivo at 0x100c640b0>: result='RunTime B: 4'
task=<generator object contador_regressivo at 0x100c640b0>: result='RunTime B: 3'
task=<generator object contador_regressivo at 0x100c640b0>: result='RunTime B: 2'
task=<generator object contador_regressivo at 0x100c640b0>: result='RunTime B: 1'
"""
