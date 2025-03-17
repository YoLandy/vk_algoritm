class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        fantom_head = ListNode()

        current = fantom_head
        a = list1
        b = list2

        while (not a is None) and (not b is None):
            if a.val <= b.val:
                current.next = a
                a = a.next
            else:
                current.next = b
                b = b.next

            current = current.next

        if b is None:
            current.next = a

        if a is None:
            current.next = b

        return fantom_head.next
