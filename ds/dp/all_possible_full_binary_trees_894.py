import datetime
from typing import List
import queue
'''
EVEN n does not result into a full binary tree.
We only can deal with odd n. 
so given n, we have check each i from 1 to n - 1 and see if i and n - 1 - i are odd. 
Only then we must distribute this recursively to left subtree and right subtree. 
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def treeUtil(self,  n):

        if n == 1:
            return [TreeNode()]
        if n == 3:
            r = TreeNode()
            r.left = TreeNode()
            r.right = TreeNode()
            return [r]

        if n <= 0:
            return []

        output = []
        for i in range(1, n-1, 2):
            if i % 2 != 0 and (n - 1 - i) % 2 != 0:
                # two cases i & n - 1 - i  and n - 1 - i & i
                X = self.treeUtil(i)
                Y = self.treeUtil(n - 1 - i)
                for x in X:
                    for y in Y:
                        r = TreeNode()
                        r.left = x
                        r.right = y
                        output.append(r)
        return output

    def allPossibleFBT(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n % 2 == 0:
            return []
        output = self.treeUtil(n)
        # print(output)
        print(len(output))
        print('------------------------------')




class SolutionWithCache(object):

    def treeUtil(self,  n, cache):

        if n in cache:
            return cache[n]

        if n == 1:
            return [TreeNode()]
        if n == 3:
            if n in cache:
                return cache[n]

            r = TreeNode()
            r.left = TreeNode()
            r.right = TreeNode()
            cache[n] = [r]
            return [r]

        if n <= 0:
            return []

        output = []
        for i in range(1, n-1, 2):
            if i % 2 != 0 and (n - 1 - i) % 2 != 0:
                # two cases i & n - 1 - i  and n - 1 - i & i
                X = self.treeUtil(i, cache)
                Y = self.treeUtil(n - 1 - i, cache)
                for x in X:
                    for y in Y:
                        r = TreeNode()
                        r.left = x
                        r.right = y
                        output.append(r)
        if n not in cache:
            cache[n] = output
        return output

    def allPossibleFBT(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n % 2 == 0:
            return []
        cache = {}
        output = self.treeUtil(n, cache)
        # print(output)
        print(len(output))

def levelOrder(root):
    q = queue.SimpleQueue()
    q.put(root)
    k = 1
    level = 0
    output = []
    while not q.empty():
        if k == q.qsize():
            print('level ', level)
            level += 1
            k = 0
        element = q.get()
        # print(element.val)
        output.append(element.val)
        if element.left is not None:
            q.put(element.left)
            k += 1
        if element.right is not None:
            q.put(element.right)
            k += 1

    print(output)


'''
copies a Tree recursivly and returns the root of newly constructed root 
'''
def copyTree(root):

    if root is None:
        return
    x = TreeNode(root.val)
    x.left = copyTree(root.left)
    x.right = copyTree(root.right)


def inorder(root):

    if root is not None:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

'''

 [
     [0,0,0,null,null,0,0,null,null,0,0],
     [0,0,0,null,null,0,0,0,0],
     [0,0,0,0,0,0,0],
     [0,0,0,0,0,null,null,null,null,0,0],
     [0,0,0,0,0,null,null,0,0]
 ]
'''
n = 17
s = Solution()
t = datetime.datetime.now()
s.allPossibleFBT(n)
e = datetime.datetime.now()
print('no cache took: {}', (e - t).total_seconds() * 1000)

t = datetime.datetime.now()
s2 = SolutionWithCache()
s2.allPossibleFBT(n)
e = datetime.datetime.now()
print('cache took: {}', (e - t).total_seconds() * 1000)






