class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        left = 0
        right = left

        while right <= len(nums) - 1:
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
                right += 1
            else:
                right += 1
