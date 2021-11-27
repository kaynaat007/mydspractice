from collections import defaultdict

class Node:

    def __init__(self, val):
        self.val = val
        self.children = [None] * 26
        self.is_last = False


class Trie:

    def __init__(self):
        pass

    def insert(self, root,  item):

        current = root

        for ch in item:

            index = ord(ch) - ord('a')
            child = current.children[index]
            if child is None:
                new_node = Node(ch)
                current.children[index] = new_node
                current = new_node

        current.is_last = True

    def search(self, root, item):

        current = root

        for ch in item:

            index = ord(ch) - ord('a')
            child = current.children[index]
            if child is None:
                return False
            if child.val != ch:
                return False
            current = child

        return True




t = Trie()
root = Node('*')
t.insert(root, 'hammer')
print(t.search(root, 'ha'))
print(t.search(root, 'ham'))
print(t.search(root, 'hr'))



