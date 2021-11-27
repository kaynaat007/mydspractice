
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def get_middle(head):

    fast = head.next
    slow = head
    if fast is not None:
        fast = fast.next
    while fast is not None:
        slow = slow.next
        fast = fast.next
        if fast is not None:
            fast = fast.next
    return slow


def get_sorted_list(left, right):

    root = None
    tail = None

    while left is not None and right is not None:
        if left.val < right.val:
            if root is not None:
                tail.next = left
                tail = left
            else:
                root = left
                tail = root
            left = left.next
        else:
            if root is not None:
                tail.next = right
                tail = right
            else:
                root = right
                tail = right

            right = right.next

        if left is not None:
            tail.next = left
        if right is not None:
            tail.next = right

    return root


def merge_sort_util(head):

    if head is None or head.next is None:
        return head

    middle = get_middle(head)
    middle_next = middle.next
    middle.next = None
    left = merge_sort_util(head)
    right = merge_sort_util(middle_next)

    return get_sorted_list(left, right)


def get_length(head):

    curr = head
    c = 0
    while curr is not None:
        curr = curr.next
        c += 1
    return c


def printList(head):

    print('------list contents ------')

    curr = head
    while curr is not None:
        print(curr.val)
        curr = curr.next


def sortList(head: ListNode) -> ListNode:

    return merge_sort_util(head)


root = ListNode(50)
root.next = ListNode(10)
root.next.next = ListNode(2)


root = ListNode(4)
root.next = ListNode(2)
root.next.next = ListNode(1)
root.next.next.next = ListNode(3)


root = ListNode(-1)
root.next = ListNode(5)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
root.next.next.next.next = ListNode(0)

root = None

root = sortList(root)
printList(root)
