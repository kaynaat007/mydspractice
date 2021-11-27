class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse(curr):

    head = curr
    while curr.next is not None:
        p = curr.next
        curr.next = p.next
        p.next = head
        head = p
    return head

def get_length(root):

    c = 0
    while root is not None:
        root = root.next
        c = c+1
    return c

def get_mid_node(root, length):

    for i in range(length//2):
        root = root.next
    return root


def isPalindrome(head: ListNode) -> bool:

        if head is None:
            return True
        root1 = head
        l = get_length(head)
        mid_node = get_mid_node(head, l)
        root2 = reverse(mid_node)
        while root1 is not None and root2 is not None:
            if root1.val != root2.val:
                return False
            root1 = root1.next
            root2 = root2.next
        return True


root = ListNode(1)
root.next = ListNode(1)
root.next.next = ListNode(0)
root.next.next.next = ListNode(0)
root.next.next.next.next = ListNode(1)


root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(2)
root.next.next.next.next = ListNode(1)


root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(1)
#
# root = ListNode(3)
#
#
# root = ListNode(1)
# root.next = ListNode(2)

print(isPalindrome(root))


