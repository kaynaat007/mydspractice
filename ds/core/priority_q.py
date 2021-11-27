"""

standard operations:

Push(x)
Pop()
Remove(x)

Issues:
    - sort stability basically return two task of same priority in same order they were inserted.
    - Tuple comparison breaks if priorities are equal and task do not have default comparison order.
    - if priority of a task changes, need to move to a new position in heap
    - if a pending task need to be delted, how do you find and remove from queue

Counter is there to break the ties between two task of same priority
It ensures task are popped out in the same order they were inserted.

Finding and deleting a task is done via an external dict which holds references to objects stored in heap
simple lookup the task you want to act upon in the dict. Dict is kept in sync with operations on queue.

Removing the entry or changing it's priority:
    if we remove and element from  heap or we change the priority, heap property may get violated.
    we can mark a task as REMOVED
    and add a new task with revised priority

"""

import heapq
from itertools import count


REMOVED = '<removed>'

class PQ:

    def __init__(self):
        self.pq = []
        self.entry_finder = {}
        self.counter = count()


    def is_empty(self):

        return len(self.entry_finder.keys()) == 0

    def add_task(self, task, priority):

        if task in self.entry_finder:
            self.remove(task)
        c = next(self.counter)
        element = [priority, c, task]
        self.entry_finder[task] = element
        heapq.heappush(self.pq, element)

    def remove(self, task):

        if task in self.entry_finder:
            element = self.entry_finder.pop(task)
            element[-1] = REMOVED

    def pop_task(self):

        while self.pq:
            priority, c, task = heapq.heappop(self.pq)
            if task is REMOVED:
                continue
            del self.entry_finder[task]
            return priority, c, task
        return None, None, None

    def print(self):
        print('---- task in priority from lowest to highest -----')
        while self.pq:
            task = self.pop_task()
            print(task)

    def decrease_priority(self, task, new_priority):

        if task not in self.entry_finder:
            return

        priority, c, task = self.entry_finder[task]
        if task is REMOVED:
            raise Exception('Task deleted')

        if new_priority > priority:
            print('new priority can be only lesser')

        self.remove(task)
        self.add_task(task, new_priority)



#
# p = PQ()
# p.add_task(0, 100)
# p.add_task(1, 101)
# p.add_task(2, 102)
#
# p.remove(2)
#
# p.print()

