class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        dp = []

        for i in range(len(s)):
            dp.append([False] * len(s))

        for i in range(len(s)):
            dp[i][i] = True

        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                dp[i][j] = self.is_palindrome(s[i : j + 1])

        # max j - i?
        for c in range(len(s), 0, -1):
            for i in range(len(s) - c):
                if dp[i][i + c]:
                    return s[i : i + c + 1]

        return s[0]

    def is_palindrome(self, line):
        if len(line) % 2:
            l = len(line) // 2
            r = l
        else:
            l = len(line) // 2 - 1
            r = l + 1

        while l > 0 and r < len(line):
            if line[l] != line[r]:
                return False
            l -= 1
            r += 1
        return True


# правильное решение которое полностью понял


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = [0, 0]

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans = [i, i + 1]

        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    ans = [i, j]

        i, j = ans
        return s[i : j + 1]
