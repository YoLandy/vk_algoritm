class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash_map = {}
        max_result = 0
        result = 0
        i = 0

        while i < len(s):
            ch = s[i]

            if ch not in hash_map:
                hash_map[ch] = i
                result += 1

            else:
                i = hash_map[ch]
                hash_map = {}
                if max_result < result:
                    max_result = result
                result = 0

            i += 1

        if max_result < result:
            max_result = result

        return max_result
