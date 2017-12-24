class Solution:
    def findLHS(self, nums):
        nums = sorted(nums)
        max_length = 0
        hash_table = {}
        for n in nums:
            hash_table.setdefault(n,0)
            hash_table[n]  = hash_table[n] + 1
        for k in hash_table:
            length = 0
            if k + 1 in hash_table:
                length = hash_table[k] + hash_table[k+1]
            if length > max_length:
                max_length = length
        return max_length


solution = Solution()
result = solution.findLHS([1,3,2,2,5,2,3,7])
print(result)
