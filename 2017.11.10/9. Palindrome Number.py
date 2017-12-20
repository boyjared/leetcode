class Solution:
    def isPalindrome(self, x):
        if x>=0 and x <10:
            return True
        if (x < 0 or x % 10 == 0):
            return False
        else:
            r_x = 0
            while(x > r_x):
                r_x = r_x*10 + x%10
                x = x//10
                print(x)
                print(r_x)
            if x == r_x or x == r_x//10 or r_x == x//10:
                return True
            else:
                return False


solution = Solution()
result = solution.isPalindrome(12321)
print(result)
