class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        first = head
        second = head

        if head is None:
            return False

        while second.next != None:
            second = second.next.next
            first = first.next
            if second is None:
                return False
            if second == first:
                return True
        return False
