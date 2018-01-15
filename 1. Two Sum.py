class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        l = len(nums)
        for i in range(0,l-1):
            n = target - nums[i]
            if n in nums[i+1:]:
                return [i, nums[i+1:].index(n)+i+1]
        return res

solution = Solution()
res = solution.twoSum([3,2,4], 6)
print(res)