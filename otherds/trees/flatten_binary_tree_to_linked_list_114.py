class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_leaf(root):
    return root.left is None and root.right is None


def util(root):

    if root is None:
        return None, None

    if is_leaf(root):
        return root, root

    head_left, tail_left = util(root.left)
    head_right, tail_right = util(root.right)

    if tail_left is not None:
        tail_left.right = head_right

    if head_left is not None:
        root.right = head_left
    else:
        root.right = head_right

    root.left = None
    return root, tail_right or tail_left


def printList(head):

    while head is not None:
        print(head.val)
        head = head.right


def flatten(root: TreeNode) -> None:
    """
    Do not return anything, modify root in-place instead.
    """
    head, tail = util(root)
    printList(head)


root = TreeNode(10)
# root.left = TreeNode(4)
root.right = TreeNode(6)

root = TreeNode(10)
root.left = TreeNode(4)
root.left.left = TreeNode(6)
root.left.left.left = TreeNode(1)

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(5)
root.right.right = TreeNode(6)


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(5)

root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
root.right.right.left = TreeNode(4)


flatten(root)

