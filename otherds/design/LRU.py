import math

class Node:

    def __init__(self, key, val, weight):
        self.weight = weight
        self.val = val
        self.key = key
        self.next = None
        self.prev = None
    def __str__(self):
        return 'key {}, val = {}, weight = {}'.format(self.key, self.val, self.weight)

class DLL:

    def __init__(self):
        self.front = None
        self.back = None

    def insert_front(self, node):
        if self.front is None:
            self.front = node
            self.front.next = None
            self.front.prev = None
            self.back = self.front
            self.back.prev = None
            self.back.next = None
        else:
            node.prev = self.front
            self.front.next = node
            self.front = node
            self.front.next = None
        return self.front

    def remove(self, node):

        prev = node.prev
        nxt = node.next
        if prev is not None:
            prev.next = nxt
        if nxt is not None:
            nxt.prev = prev
        if self.back is node:
            self.back = nxt
        if self.front is node:
            self.front = prev
        return node

    def print(self):
        print('------- DLL Elements -------')
        curr = self.back
        print('back element: {}, front element {}'.format(self.back, self.front))
        while curr is not None:
            print(curr)
            curr = curr.next


class LRUCache:

    def __init__(self, capacity: int):
        self.n = capacity
        self.ds = {}
        self.max_weight = 0
        self.dll = DLL()

    def get(self, key: int) -> int:
        """
        if key not in cache
            add it to cache with weight = max_weight + 1
        else:
            get node
            increment weight = max_weight + 1
            remove this node
            put this node in front
            update max_weight
        """
        if key not in self.ds:
            return -1
        node = self.ds[key]
        self.max_weight += 1
        node.weight = self.max_weight
        self.dll.remove(node)
        self.dll.insert_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        """
        if space full:
            take back-node
            remove it
            add incoming node to front
            update node's weight with max_weight + 1
            set max_weight to new weight
        else:
            make a node
            set its weight
            add it to front
        """
        self.max_weight += 1
        if key in self.ds:
            node = self.ds[key]
            self.dll.remove(node)
            node.val = value
            node.weight = self.max_weight
            self.dll.insert_front(node)
        else:
            if self.n == len(self.ds.keys()):
                node = self.dll.back
                del self.ds[node.key]
                self.dll.remove(self.dll.back)
            node = Node(key, value, self.max_weight)
            node = self.dll.insert_front(node)
            self.ds[key] = node

    def print(self):

        print('\n------- LRU --------')
        self.dll.print()


lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1))
lru.put(3, 3)
print(lru.get(2))
lru.put(4, 4)
print(lru.get(1))
print(lru.get(3))
print(lru.get(4))
lru.print()
lru.put(4, 10)
print(lru.get(4))
lru.print()






# lru.put(3, 10)
# lru.print()