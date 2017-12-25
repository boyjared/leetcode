class Solution:
    def isPerfectSquare(self, num):
        flag = False
        i = 1
        while(num/i >= i):
            if(num/i == i):
                flag = True
                break
            else:
                i = i+1
        return flag

solution = Solution()
result = solution.isPerfectSquare(1)
print(result)