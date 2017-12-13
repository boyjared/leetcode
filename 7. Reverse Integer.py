import math

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 :
            return 0
        if x > 0:
            s = str(x)
            r_x = int(s[::-1])
            if r_x > math.pow(2,31)-1:
                return 0
            else:
                return r_x
        if x < 0:
            s = str(-x)
            n_x = int(s[::-1])
            if n_x > math.pow(2,31)-1:
                return 0
            else:
                return -n_x

solution = Solution()
result = solution.reverse(1563847412)
print(result)
