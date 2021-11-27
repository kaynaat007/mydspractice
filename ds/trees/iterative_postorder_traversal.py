class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def visit(node):
    print(node.val)


def iterative_postorder(root):

    stack = []
    current = root
    while True:
        if current is not None:  # IF CURRENT is not NONE
            stack.append(current)
            current = current.left
            continue
        else:  # if current is none, means we are extreme left
            last_stack = None

            while stack:  # popping
                top = stack[-1]
                if top.right is None:
                    last_stack = stack.pop()
                else:
                    if last_stack and last_stack == top.right:
                        last_stack = stack.pop()
                    else:
                        break
                visit(last_stack)

            if not stack:
                # finish here
                break
            top = stack[-1]
            current = top.right

root = TreeNode(6)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(5)
root.right = TreeNode(8)
root.right.left = TreeNode(7)
root.right.left.left = TreeNode(4)


print(iterative_postorder(root))


