# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self):
        self.root = None

    def util(self, curr):
        if curr is None:
            return None
        if curr.next is None:
            self.root = curr

        tail = self.util(curr.next)
        curr.next = None
        if tail is not None:
            tail.next = curr
            tail = curr
        else:
            tail = curr
        return tail

    def util_stack(self, curr):

        self.root = curr
        while curr.next is not None:
            p = curr.next
            curr.next = p.next
            p.next = self.root
            self.root = p
        return self.root

    def reverseList(self, head: ListNode) -> ListNode:
        # self.util(head)
        self.util_stack(head)
        return self.root

    def print(self, root):

        print("current list --> ")
        while root is not None:
            print(root.val)
            root = root.next
        print("--------")
        return root

head = ListNode(10)
head.next = ListNode(12)
head.next.next = ListNode(15)
head.next.next.next = ListNode(20)

s = Solution()
print(s.print(head))
head = s.reverseList(head)
print(s.print(head))



