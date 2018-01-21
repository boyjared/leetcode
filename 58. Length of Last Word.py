class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        list_s = s.split(" ")
        for c in reversed(list_s):
            if c != '':
                return len(c)
        return 0

s = Solution()
r = s.lengthOfLastWord("fe fe fef ")
print(r)