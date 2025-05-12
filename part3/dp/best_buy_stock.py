class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = prices[0]
        sell = prices[0]
        best_price = 0

        for num in prices:
            if num < buy:
                buy = num
                sell = num
                continue

            if num >= sell:
                sell = num
                if sell - buy > best_price:
                    best_price = sell - buy

        return max(best_price, sell - buy)
