from typing import List

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


def util(s, i, j, n):

    if i > j:
        return

    v = s[i]
    root = TreeNode(v)
    val = root.val

    k = i + 1
    while k <= j < n:
        v = s[k]
        if v >= val:
            break
        k += 1

    root.left = util(s, i+1, k-1, n) #
    root.right = util(s, k , j, n)

    return root

def bstFromPreorder(preorder: List[int]) -> TreeNode:

    return util(preorder, 0, len(preorder)-1, len(preorder))

preorder = [5, 1, 6]
preorder = [6, 5, 1]
preorder = [8,5,1,7,10,12]
root = bstFromPreorder(preorder)
printTree(root)

