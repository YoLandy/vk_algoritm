# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.is_sym(root.left, root.right)

    def is_sym(self, a, b):
        if a is None and b is None:
            return True
        if any([a is None, b is None]):
            return False
        if a.val != b.val:
            return False
        return self.is_sym(a.left, b.right) and self.is_sym(a.right, b.left)
