

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printList(head):

    while head:
        print(head.val)
        head = head.next


def oddEvenList(head: ListNode) -> ListNode:

    if not head:
        return None

    first_head = head
    second_head = head.next
    head1 = head
    head2 = head.next
    tail = None
    while first_head and second_head:

        first_next = second_head.next
        first_head.next = first_next

        second_next = None
        if first_next:
            second_next = first_next.next
            second_head.next = second_next
        tail = first_next or first_head
        first_head = first_next
        second_head = second_next

    if tail:
        tail.next = head2

    return head1

head = ListNode(10)
head.next = ListNode(12)
head.next.next = ListNode(13)
head.next.next.next = ListNode(15)
head.next.next.next.next = ListNode(16)

print(oddEvenList(head))














