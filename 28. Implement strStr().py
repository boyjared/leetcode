class Solution:
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        elif needle in haystack and needle!= "":
            arr = haystack.split(needle)
            print(arr)
            return len(arr[0])
        return -1

solution = Solution()
s="abcdebc"
val="bc"
result=solution.strStr(s, val)
print(result)
