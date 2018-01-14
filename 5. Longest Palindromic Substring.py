class Solution:
    def longestPalindrome(self, s):

        def expandAroundCenter(s, left, right):
            L = left
            R = right
            while(L>=0 and R<len(s) and s[L] == s[R]):
                L -= 1
                R += 1
            return R-L-1

        start = 0
        end = 0
        len_s = len(s)
        for i in range(0, len_s):
            len1 = expandAroundCenter(s, i, i)
            len2 = expandAroundCenter(s, i, i+1)
            l = max(len1, len2)
            if l > end - start:
                start = i-(l-1)//2
                end = i+l//2

        return s[start:end+1]




solution = Solution()
res = solution.longestPalindrome("babad")
print(res)