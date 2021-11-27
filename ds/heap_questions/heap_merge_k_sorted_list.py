import math
import heapq

'''

initialize a min heap of size k
populate with first elements of each list 

while heap is not empty: 

    extract min and print the output 
    shift the next pointer of the extracted node to point to next node. 
    Insert this node into heap

'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Heap:

    def __init__(self, A):
        self.A = A
        self.heap_size = len(A)

    def get_size(self):
        return self.heap_size

    def print(self):

        print('------------------------------')

        for i in range(self.heap_size):
            node = self.A[i]
            print("val={}".format(node.val))

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return  2 * i + 2

    def swap(self, i, j):
        t = self.A[i]
        self.A[i] = self.A[j]
        self.A[j] = t

    def parent(self, i):

        if i == 0:
            return 0
        return math.floor( (i-1) / 2)

    def build_heap(self):

        n = len(self.A)
        for i in range(math.floor(n/2), -1, -1):
            self.heapify(i)

    def heapify(self, i):

        left_index = self.left(i)
        right_index = self.right(i)

        if left_index >= 0 and right_index <= self.heap_size-1:

            min_index = i
            if self.A[i].val > self.A[left_index].val:
                min_index = left_index

            if self.A[min_index].val > self.A[right_index].val:
                min_index = right_index

            if min_index != i:

                self.swap(i, min_index)
                self.heapify(min_index)

        elif 0 <= right_index <= self.heap_size-1:

            if self.A[i].val > self.A[right_index].val:
                self.swap(i, right_index)
                self.heapify(right_index)

        elif 0 <= left_index <= self.heap_size-1:

            if self.A[i].val > self.A[left_index].val:

                self.swap(i, left_index)
                self.heapify(left_index)

    def get_min(self):

        return self.A[0]

    def get_total_size(self):

        return len(self.A)

    def extract_min(self):

        min_node = self.A[0]
        self.A[0] = self.A[self.heap_size-1]
        self.heap_size -= 1
        self.heapify(0)
        return min_node

    def insert(self, e):

        null_node = ListNode()

        if self.heap_size == self.get_total_size():
            self.A.append(null_node)
            self.heap_size += 1
        else:
            self.heap_size += 1
            self.A[self.heap_size - 1] = null_node

        self.decrease_key(self.heap_size - 1, e)

    def decrease_key(self, i, e):
        #
        # if  e.val > self.A[i].val:
        #     return

        self.A[i] = e

        while i >= 0 and self.A[self.parent(i)].val > e.val:
            self.swap(self.parent(i), i)
            i = self.parent(i)


# please see that here input is 2D matrix of numbers only while in
# question it is a single list containing a bunch of linked list.

input =[

    [9, 10, 25],
    [5, 10, 20],
    [1, 10, 20]

]

A = []

n = len(input)
m = len(input[0])


def custom_heap_implementation():

        k = 0
        heads = []
        for i in range(n):
            head = None
            current = None
            for j in range(len(input[i])):
                if current is None:
                    head = ListNode(input[i][j])
                    current = head
                else:
                    node = ListNode(input[i][j])
                    current.next = node
                    current = node
            heads.append(head)

        heap = Heap(heads)
        heap.build_heap()

        while heap.get_size() > 0:

            min_node = heap.extract_min()
            print(min_node.val)
            next_node = min_node.next
            if next_node:
                heap.insert(next_node)


"""

python builtin heapq implementation. 
use of a tuple (a, b, c) as an element of heap. 
break the tie by keeping a unique variable count as second element in the tuple. 


"""


def with_heapq_ds(lists):

    n = len(lists)
    if n == 0:
        return None

    q = []
    count = 0
    for i in range(n):
        head = lists[i]
        if head:
            heapq.heappush(q, (head.val, count, head))

    if not q:
        return None
    head = None
    current = None
    while q:
        val, node = heapq.heappop(q)
        if current is None:
            head = node
            current = head
        else:
            current.next = node
            current = node
        if node.next:
            heapq.heappush(q, (node.next.val, count, node.next))
            count += 1
    return head