from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def printTree(root):

    if root is not None:
        printTree(root.left)
        print(root.val)
        printTree(root.right)


class Construct:

    def __init__(self):
        self.k = 0

    def util(self, i, j, preorder, inorder):

        if i > j:
            return

        val = preorder[self.k]
        self.k +=1
        root_index = self.lookup[val]
        root = TreeNode(val)
        root.left = self.util(i, root_index-1,  preorder, inorder)
        root.right = self.util(root_index + 1, j, preorder, inorder)
        return root


    def buildTree(self, preorder: List[int], inorder_list: List[int]) -> TreeNode:
        """

        """
        if not preorder:
            return None
        self.lookup = {val: i for i, val in enumerate(inorder_list)}
        return self.util(0, len(inorder_list)-1, preorder, inorder_list)



preorder = [3,9,20,15,7]
inorder_list = [9,3,15,20,7]


#
# preorder = [2,1,3]
# inorder_list = [1,2,3]

# preorder = [2]
# inorder_list = [2]


# preorder = [2,1,3]
# inorder_list = [3,1,2]

obj = Construct()
root = obj.buildTree(preorder, inorder_list)
printTree(root)

