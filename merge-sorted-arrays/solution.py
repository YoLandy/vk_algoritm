class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        writer = m + n - 1
        right1 = m - 1
        right2 = n - 1

        while right2 >= 0:
            if nums1[right1] >= nums2[right2] and right1 >= 0:
                nums1[writer], nums1[right1] = nums1[right1], nums1[writer]
                right1 -= 1

            else:
                nums1[writer] = nums2[right2]
                right2 -= 1

            writer -= 1
