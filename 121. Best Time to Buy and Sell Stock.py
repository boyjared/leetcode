class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) != 0:
            lowest = prices[0]
        else:
            return 0
        max_profit = 0
        for n in prices:
            profit = n - lowest
            lowest = min(n, lowest)
            max_profit = max(max_profit, profit)
        return max_profit

solution = Solution()
result = solution.maxProfit([2,1])
print(result)