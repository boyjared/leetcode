class Solution:
    def checkValidString(self, s):
        lo = hi = 0
        for c in s:
            if c == '(':
                lo = lo + 1
            else:
                lo = lo - 1
            if c != ')':
                hi = hi + 1
            else:
                hi = hi - 1
            if hi < 0:
                break
            lo = max(lo, 0)
        if lo == 0:
            return True
        else:
            return False

solution = Solution()
result = solution.checkValidString("())")
print(result)