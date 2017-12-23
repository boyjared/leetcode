class Solution:
    def minCostClimbingStairs(self, cost):
        f1 = f2 = 0
        for x in reversed(cost):
            f1, f2 = x + min(f1, f2), f1
        return min(f1, f2)

solution = Solution()
result = solution.minCostClimbingStairs([10, 15, 20])
print(result)