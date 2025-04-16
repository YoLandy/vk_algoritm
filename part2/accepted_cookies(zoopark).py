class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()

        count = 0
        for si in s:
            if si >= g[count]:
                count += 1

            if count == len(g):
                break

        return count
