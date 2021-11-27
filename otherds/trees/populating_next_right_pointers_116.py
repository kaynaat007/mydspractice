from collections import deque

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect_util(root, parent):

    if root is None:
        return
    if parent is None:
        root.next = None
    else:
        if parent.left == root:
            root.next = parent.right
        elif parent.next is not None:
            root.next = parent.next.left
        else:
            root.next = None

    connect_util(root.left, root)
    connect_util(root.right, root)


def connect(root: 'Node') -> 'Node':

    connect_util(root, None)
    return root

def connect_bfs(root: 'Node') -> 'Node':

    connect_util_bfs(root)
    return root


def connect_util_bfs(root):

    q = deque([root])
    while q:
        current = q.popleft()

        right_child = current.right
        left_child = current.left

        if left_child:
            left_child.next = right_child

        if right_child and current.next:
            right_child.next = current.next.left

        if left_child:
            q.append(left_child)
        if right_child:
            q.append(right_child)

    return root




def inorder(root):

    if root:
        inorder(root.left)
        if root.next is None:
            print(root.val, 'None')
        else:
            print(root.val, root.next.val)
        inorder(root.right)


root = Node(val=1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)


# root_ = connect(root)

root_ = connect_util_bfs(root)

inorder(root_)

