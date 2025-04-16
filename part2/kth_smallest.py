# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        sorted_arr = self.lnr(root, [])
        return sorted_arr[k - 1]

    def lnr(self, root, data):
        if root is None:
            return data
        data = self.lnr(root.left, data)
        data.append(root.val)
        data = self.lnr(root.right, data)
        return data
