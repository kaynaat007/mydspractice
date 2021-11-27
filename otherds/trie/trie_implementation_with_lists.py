"""
This implementation of Trie uses array indices
"""

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
            else:
                current = child

        current.is_last = True

    def search(self, root, item):

        current = root

        for ch in item:

            index = ord(ch) - ord('a')
            child = current.children[index]
            if child is None:
                return False
            current = child

        return True if current.is_last else False

    def startsWith(self, root,  prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """

        current = root
        for ch in prefix:
            index = ord(ch) - ord('a')
            child = current.children[index]
            if not child:
                return False
            current = child

        return True

root = Node('*')
t = Trie()
t.insert(root, 'apple')
print(t.search(root, 'apple'))
print(t.search(root, 'app'))
print(t.startsWith(root, 'app'))
t.insert(root, 'app')
print(t.search(root, 'app'))
