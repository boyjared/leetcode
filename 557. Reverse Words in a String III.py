class Solution:
    def reverseWords(self, s):
        result = ""
        s_arr = s.split(" ")
        for i in range(len(s_arr)):
            if(i != len(s_arr)-1):
                result = result + s_arr[i][::-1] + " "
            else:
                result = result + s_arr[i][::-1]
        return result

solution = Solution()
s = "hehe hehe hehe hehe"
result = solution.reverseWords(s)
print(result)




