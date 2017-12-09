class Solution:
    def repeatedSubstringPattern(self, s):
        return s in (s*2)[1:-1]

solution = Solution()
s = "abcabc"
result = solution.repeatedSubstringPattern(s)
print(result)

