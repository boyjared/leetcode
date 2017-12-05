class Solution:

    def palindrome(self, s):
        return (s[::-1] == s)

    def validDelPalindrome(self, s, i):
        l = len(s) - 1
        result = False
        s1 = s[:i] + s[i+1:]
        s2 = s[:l-i] + s[l-i+1:]
        s3 = s[1:]
        s4 = s[: l]

        result = (self.palindrome(s1) or self.palindrome(s2) or self.palindrome(s3) or self.palindrome(s4))
        return result

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = len(s) - 1
        n = len(s)//2
        for i in range(0,n):
            if s[i] != s[l-i]:
                return self.validDelPalindrome(s, i)
        return (self.palindrome(s))

solution = Solution()
res = solution.validDelPalindrome("abbaaaa", 1)

print(res)