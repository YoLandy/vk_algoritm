class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        middle = 0

        if len(nums) == 1:
            return

        while middle <= right:
            if nums[middle] == 2:
                nums[middle], nums[right] = nums[right], nums[middle]
                right -= 1
            elif nums[middle] == 0:
                nums[middle], nums[left] = nums[left], nums[middle]
                left += 1
                middle += 1
            elif nums[middle] == 1:
                middle += 1
