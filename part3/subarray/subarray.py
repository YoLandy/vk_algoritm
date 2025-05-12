class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dp = {}
        dp[0] = 1

        count = 0
        prefsum = 0

        for i in range(len(nums)):
            prefsum += nums[i]

            if prefsum - k in dp:
                count += dp[prefsum - k]

            if prefsum in dp:
                dp[prefsum] = dp[prefsum] + 1
            else:
                dp[prefsum] = 1

        return count
