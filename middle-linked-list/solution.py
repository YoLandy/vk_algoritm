class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        current = head
        middle = head

        while current.next != None and current.next.next != None:
            current = current.next.next
            middle = middle.next

        return middle
