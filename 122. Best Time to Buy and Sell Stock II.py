class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        if len(prices) == 1:
            return 0
        if len(prices) == 2:
            if prices[1] > prices[0]:
                return prices[1] - prices[0]
            else:
                return 0
        lowest = prices[0]
        highest = 0
        sum_profit = 0
        i = 0
        while(i < (len(prices) - 1)):
            while(i < (len(prices) - 1) and prices[i] >= prices[i+1]):
                i = i+1
                lowest = prices[i]
            while(i < (len(prices) - 1) and prices[i] < prices[i+1]):
                i = i+1
                highest = prices[i]
            if highest > lowest:
                sum_profit = sum_profit + highest - lowest
            highest = 0
            lowest = prices[i]
        return sum_profit

solution = Solution()
result = solution.maxProfit([1,2,4])
print(result)