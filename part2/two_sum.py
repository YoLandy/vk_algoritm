class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        data = dict()

        for i, num in enumerate(nums):
            if num not in data:
                data[num] = i
            elif num * 2 == target:
                return (i, data[num])

        for num in data:
            a = target - num
            if a in data and data[a] != data[num]:
                return (data[num], data[a])
