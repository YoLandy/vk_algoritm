class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head

        current_before = head
        current = head.next

        head.next = None

        while current.next != None:
            current_next = current.next
            current.next = current_before
            current_before = current
            current = current_next
        current.next = current_before
        return current
