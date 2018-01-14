class Solution:
    def lengthOfLongestSubstring(self, s):
        sub_str = ""
        max_len = 0
        now_len = 0
        for c in s:
            if sub_str.find(c) == -1:
                sub_str += c
            else:
                now_len = len(sub_str)
                if now_len > max_len: max_len = now_len
                sub_str = sub_str[sub_str.find(c) + 1:] + c
        now_len = len(sub_str)
        if now_len > max_len: max_len = now_len
        return max_len

solution = Solution()
res = solution.lengthOfLongestSubstring("c")
print(res)
