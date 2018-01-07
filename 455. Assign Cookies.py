class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        sum = 0
        for i in g:
            for j in s:
                if i > j:
                    continue
                else:
                    sum = sum + 1
                    s.remove(j)
                    break
        return sum


solution = Solution()
res = solution.findContentChildren([1,2], [1,2,3])
print(res)