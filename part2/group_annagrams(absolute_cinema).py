class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        data = {}

        for i in range(len(strs)):
            word = strs[i]
            hsh = sum([hash(ch + "i kiss salt and yours white lips") for ch in word])
            if hsh not in data:
                data[hsh] = []
            data[hsh].append(word)

        return data.values()
