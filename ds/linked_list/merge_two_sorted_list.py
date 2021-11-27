'''

Follow simple strategy of merge sorting 
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_list(head):

    print('--------')
    while head is not None:
        print(head.val)
        head = head.next


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:

    head = None

    if not l1:
        root = l2
    elif not l2:
        root = l1
    else:
        if l1.val <= l2.val:
            root = l1
        else:
            root = l2

    while l1 is not None and l2 is not None:

        if l1.val <= l2.val:
            if head:
                head.next = l1
                head = l1
            else:
                head = l1
            l1 = l1.next


        else:
            if head:
                head.next = l2
                head = l2
            else:
                head = l2
            l2 = l2.next


    while head is not None and l1 is not None:
        head.next = l1
        head = l1
        l1 = l1.next

    while head is not None and l2 is not None:
        head.next = l2
        head = l2
        l2 = l2.next

    return root


l1 = ListNode(3)
l1.next = ListNode(5)
l1.next.next = ListNode(6)

l2 = ListNode(1)
l2.next = ListNode(1)

l1 = ListNode(1)
l1.next = ListNode(2)


l2 = ListNode(0)
l2.next = ListNode(1)

print_list(mergeTwoLists(l1, l2))






