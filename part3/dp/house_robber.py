class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) >= 3:
            nums[2] += nums[0]

        else:
            if len(nums) == 2:
                return max(nums[0], nums[1])
            elif len(nums) == 1:
                return nums[0]
            else:
                return 0

        for i in range(3, len(nums)):
            nums[i] += max(nums[i - 2], nums[i - 3])

        return max(nums[-1], nums[-2])
