class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dp = []

        for i in range(10):
            line = []
            for j in range(10):
                line.append((i + j) % 10)
            dp.append(line)

        n = len(nums) - 1

        for _ in range(n):
            newNums = [0] * (len(nums) - 1)

            for i in range(len(nums) - 1):
                newNums[i] = dp[nums[i]][nums[i + 1]]

            nums = newNums

        return nums[0]
