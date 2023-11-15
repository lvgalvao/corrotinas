from collections import deque


def contador(stop):
    cont = 1
    while cont <= stop:
        cont += 1
        return cont


def contador_regressivo(start):
    while start >= 1:
        start -= 1
        return start


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
Scheduler(deque([2, 4]))
>>> s.run()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/lucianogalvao/github/corrotinas/exemplo_01.py", line 28, in run
    result = next(task)
TypeError: 'int' object is not an iterator
"""
