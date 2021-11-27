class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def to_dll(root, head_ref):

    # head = head_ref[0]
    if head_ref[0]:
        print('current head ref: {}'.format(head_ref[0].val))
    else:
        print('head ref is None')

    if root is not None:
        to_dll(root.left, head_ref)
        if head_ref[0] is None:  # a check to make sure head is not initialized to anything
            head_ref[0] = root
            head_ref[0].left = None
            head_ref[0].right = None
            print('head ref is None setting head to: {}'.format(head_ref[0].val))
        else:
            head_ref[0].right = root
            root.left = head_ref[0]
            head_ref[0] = root
            print('setting head to: {}'.format(head_ref[0].val))
        # head_ref[0] = head
        to_dll(root.right, head_ref)


def flatten(root: TreeNode) -> None:
    """
    Do not return anything, modify root in-place instead.
    """
    tail = None
    ref = [None]
    to_dll(root, ref)
    # tail = head_ref[0]
    head_ref = ref[0]
    print_dll(head_ref)


def print_dll(tail):
    print('printing DLL...')

    while tail is not None:
        print(tail.val)
        tail = tail.left


# root = TreeNode(10)
# root.left = TreeNode(4)
# root.left.left = TreeNode(6)
# root.left.left.left = TreeNode(1)

root = TreeNode(10)
root.left = TreeNode(4)
root.right = TreeNode(6)

root = TreeNode(10)
root.left = TreeNode(12)
root.left.right = TreeNode(30)
root.left.left = TreeNode(25)
root.right = TreeNode(15)
root.right.left = TreeNode(36)

flatten(root)
