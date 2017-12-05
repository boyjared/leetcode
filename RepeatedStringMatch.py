# -*- coding: utf-8 -*-

class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if len(B) > len(A):
            n = len(B)//len(A) * 3
        else:
            n = len(A)//len(B) * 3
        str_A = ''
        for i in range(1, n):
            str_A = str_A + A
            if(B in str_A):
                return i
        return -1

solution = Solution()
result = solution.repeatedStringMatch("abc", "aabcbabcc")
print(result)