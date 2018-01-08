class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for n in nums:
            count.setdefault(n, 0)
            count[n] += 1
        s = sorted(count.items(), key = lambda item:item[1], reverse=True)
        return s[0][0]

solution = Solution()
res = solution.majorityElement([2,1,-1,-1,-1])
print(res)