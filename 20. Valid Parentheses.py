class Solution:

    def isValid(self, s):
        match_dict = {'(':')', "{":"}", "[":"]"}
        stack = []
        for c in s:
            if c in match_dict.keys():
                stack.append(c)
            elif len(stack) != 0 and match_dict[stack.pop()] == c:
                continue
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False

solution = Solution()
s = "]"
result = solution.isValid(s)
print(result)

