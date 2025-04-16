# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        level = 0
        queue = [root]

        if not root:
            return 0

        stop = False
        while len(queue) > 0:
            new_queue = []
            for node in queue:
                if node.left is None and node.right is None:
                    stop = True
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            queue = new_queue
            level += 1
            if stop:
                break

        return level
