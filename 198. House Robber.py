class Solution:
    def rob(self, nums):
        tmp = 0
        i = 0
        e = 0
        for n in nums:
            tmp = i
            i = e + n
            e = max(tmp,e)
        return max(i, e)
solution = Solution()
result = solution.rob([1,2,3,4])
print(result)
