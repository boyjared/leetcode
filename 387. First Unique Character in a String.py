class Solution:
    def firstUniqChar(self, s):
        l = len(s)
        repeat = []
        for i in range(0, l):
            c = s[i]
            if i == l-1:
                if s.find(c) == i:
                    return i
                else:
                    return -1
            elif s[i+1:].find(c) != -1:
                repeat.append(c)
                continue
            elif c not in repeat:
                return i
        return -1

solution = Solution()
s = "aadadaad"
result = solution.firstUniqChar(s)
print(result)
