from trees import bst
import math

"""
how will you print out all modes of a sorted array ? 
in one pass you fill find the maximum occuring frequency. 
in the second pass, you will print the elements occurring with that frequency 

same is applied in a BST. 

"""

class Solution:


    def find_max_freq(self, root):

        if root is not None:
            self.find_max_freq(root.left)
            if self.val is not None and root.val == self.val:
                self.freq += 1
            else:
                self.freq = 1
                self.val = root.val
            self.ans = max(self.ans, self.freq)
            self.find_max_freq(root.right)

    def find_mode_util(self, root):

        if root is not None:
            self.find_mode_util(root.left)

            if self.val is not None and root.val == self.val:
                self.freq += 1
                if self.freq == self.ans:
                    self.output.append(root.val)
            else:
                self.freq = 1
                self.val = root.val
                if self.freq == self.ans:
                    self.output.append(root.val)

            self.find_mode_util(root.right)

    def findMode(self, root: bst.Node):

        self.freq = 0
        self.ans = 0
        self.val = None
        self.output = []

        self.find_max_freq(root)
        self.val = math.inf
        self.freq = 0
        self.find_mode_util(root)

        return self.output


bst = bst.BST()
# bst.init(1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7)

# bst.init(2147483647)

bst.init(0, 0)
# bst.init(10)

s = Solution()
s.findMode(bst.root)
print(s.output)





