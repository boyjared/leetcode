class Solution:
    def strStr(self, haystack, needle):
        # if needle == "":
        #     return 0
        # elif needle in haystack:
        #     arr = haystack.split(needle)
        #     print(arr)
        #     return len(arr[0])
        # return -1
        return haystack.find(needle)

solution = Solution()
s="aaaaa"
val=""
result=solution.strStr(s, val)
print(result)
