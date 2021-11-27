import math
class MinHeap:

    def swap(self, i, j):
        t = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = t

    def __init__(self):
        self.heap = []
        self.n = 0

    def parent(self, i):

        if i % 2 == 0:
            return i // 2 - 1
        return i // 2

    def insert(self, e):

        self.n += 1
        self.heap.append(e)
        p = self.parent(self.n-1)
        j = self.n-1
        while p >= 0 and self.heap[p] > e:
            self.swap(p, j)
            j = p
            p = self.parent(p)

    def extract(self):

        if self.n >= 1:
            e = self.heap[0]
            self.swap(0, self.n-1)
            del self.heap[self.n-1]
            self.n -= 1
            if self.n > 0:
                self.heapify(0)
            return e

    def build_heap(self):

        for i in range(self.n//2, -1, -1):
            self.heapify(i)

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def heapify(self, i):

        e = self.heap[i]
        left_child_index = self.left(i)
        right_child_index = self.right(i)

        min_index = i

        if 0 <= left_child_index < self.n and 0 <= right_child_index < self.n:

            if self.heap[left_child_index] < self.heap[right_child_index]:
                min_index = left_child_index
            else:
                min_index = right_child_index
        elif 0 <= left_child_index < self.n:

            if e > self.heap[left_child_index]:
                min_index = left_child_index

        elif 0 <= right_child_index < self.n:

            if e > self.heap[right_child_index]:
                min_index = right_child_index

        if min_index != i and e > self.heap[min_index]:
            self.swap(i, min_index)
            self.heapify(min_index)

    def get_min(self):

        if self.heap:
            return self.heap[0]

    def print(self):

        while self.n:
            # print('size: {}'.format(self.n))
            print(self.extract())


class MaxHeap:

    def swap(self, i, j):
        t = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = t

    def __init__(self):
        self.heap = []
        self.n = 0

    def parent(self, i):

        if i % 2 == 0:
            return i // 2 - 1
        return i // 2

    def insert(self, e):

        self.n += 1
        self.heap.append(e)
        p = self.parent(self.n-1)
        j = self.n-1
        while p >= 0 and self.heap[p] < e:
            self.swap(p, j)
            j = p
            p = self.parent(p)

    def extract(self):

        if self.n >= 1:
            e = self.heap[0]
            self.swap(0, self.n-1)
            del self.heap[self.n - 1]
            self.n -= 1
            if self.n > 0:
                self.heapify(0)
            return e


    def build_heap(self):

        for i in range(self.n//2, -1, -1):
            self.heapify(i)

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def heapify(self, i):

        e = self.heap[i]
        left_child_index = self.left(i)
        right_child_index = self.right(i)

        max_index = i

        if 0 <= left_child_index < self.n and 0 <= right_child_index < self.n:

            if self.heap[left_child_index] > self.heap[right_child_index]:
                max_index = left_child_index
            else:
                max_index = right_child_index
        elif 0 <= left_child_index < self.n:

            if e < self.heap[left_child_index]:
                max_index = left_child_index

        elif 0 <= right_child_index < self.n:

            if e < self.heap[right_child_index]:
                max_index = right_child_index

        if max_index != i and e < self.heap[max_index]:
            self.swap(i, max_index)
            self.heapify(max_index)

    def get_max(self):

        if self.heap:
            return self.heap[0]

    def print(self):

        while self.n:
            # print('size: {}'.format(self.n))
            print(self.extract())

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left_heap  = MaxHeap()
        self.right_heap = MinHeap()
        self.median = None

    def get_median(self):

        n1 = self.left_heap.n
        n2 = self.right_heap.n

        if (n1 + n2) % 2 == 0:
            return (self.left_heap.get_max() + self.right_heap.get_min())/2
        else:
            if n1 > n2:
                return self.left_heap.get_max()
            else:
                return self.right_heap.get_min()

    def addNum(self, num: int) -> None:
        """
        compare num with median
        if less, push to left heap
        if more, push to right heap
        """
        if self.median is None:
            self.median = num
            self.left_heap.insert(num)
        else:
            left_size = self.left_heap.n
            right_size = self.right_heap.n
            if num < self.median:
                if left_size <= right_size:
                    self.left_heap.insert(num)
                else:
                    left_top_val = self.left_heap.extract()
                    self.right_heap.insert(left_top_val)
                    self.left_heap.insert(num)
            else:
                if right_size <= left_size:
                    self.right_heap.insert(num)
                else:
                    right_top_val = self.right_heap.extract()
                    self.left_heap.insert(right_top_val)
                    self.right_heap.insert(num)

        self.median = self.get_median()


    def findMedian(self) -> float:
        """
        pass
        """
        return self.median

# med = MinHeap()
# med = MaxHeap()
#
# med.insert(3)
# med.insert(4)
# med.insert(2)
#
# med.insert(6)


mf = MedianFinder()

# mf.addNum(5)
# mf.addNum(3)
# mf.addNum(10)
# mf.addNum(12)
# mf.addNum(2)
# mf.addNum(7)

mf.addNum(1)
mf.addNum(2)
print(mf.findMedian())
mf.addNum(3)
print(mf.findMedian())









