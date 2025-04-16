class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dick_t = {}

        for ch in s:
            if ch not in dick_t:
                dick_t[ch] = 0
            dick_t[ch] += 1

        for ch in t:
            if ch in dick_t:
                dick_t[ch] -= 1
                if dick_t[ch] < 0:
                    return ch
            else:
                return ch
