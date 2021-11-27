class Trie:

    def __init__(self):

        self.trie = {}

    def insert(self, word):

        current = self.trie
        for w in word:

            if w not in current:
                current[w] = {}
            current = current[w]
        current['#'] = '#'

    def search(self, word):

        current = self.trie
        for w in word:
            if w not in current:
                return False
            current = current[w]
        return True if '#' in current else False

    def prefix(self, prefix):

        current = self.trie
        for w in prefix:
            if w not in current:
                return False
            current = current[w]

        return True


t = Trie()
t.insert('apple')
print(t.search('apple'))
print(t.search('app'))
print(t.prefix('app'))
t.insert('app')
print(t.search('app'))
