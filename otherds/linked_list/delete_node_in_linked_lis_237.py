"""
O(n) time for deletion since pointer to node to be deleted will be privided.
adjust some pointers.

"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteNode(node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    while node.next is not None:
        node.val = node.next.val
        p = node
        node = node.next
    p.next = None


def printList(root):

    while root:
        print(root.val)
        root = root.next

# t = ListNode(10)
# t.next = ListNode(12)
# p = t.next
# t.next.next = ListNode(13)


# t = ListNode(4)
# t.next = ListNode(5)
# t.next.next = ListNode(1)
# t.next.next.next = ListNode(9)
#
# p = t.next
# p = t.next.next

t = ListNode(-3)
t.next = ListNode(5)
t.next.next = ListNode(-99)

p = t

deleteNode(p)

printList(t)

