from functools import reduce
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ""
        def commonPrefix(str1, str2):
            l = min(len(str1), len(str2))
            res = ""
            for i in range(l):
                if str1[i] == str2[i]:
                    res += str1[i]
                else:
                    break
            return res

        return reduce(commonPrefix, strs)

solution = Solution()
res = solution.longestCommonPrefix(["1","1"])
print(res)

