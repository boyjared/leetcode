class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        else:
            dup_num = 0
            total_len = len(nums)
            i = 1
            while(i < len(nums) and len(nums) > 1):
                dup = False
                while(dup == False and i < len(nums) and len(nums) > 1):
                    j = i-1
                    if nums[j] == nums[i]:
                        dup = True
                        dup_num += 1
                        nums.remove(nums[j])
                        i = j+1
                    else:
                        i += 1
            return total_len - dup_num

solution = Solution()
res = solution.removeDuplicates([1,1,2,3,3])
print(res)