class Solution:
    def longestPalindrome(self, s):

        def isPalindrome(s):
            return s == s[::-1]

        max_len = 0
        max_sub_palStr = ""
        now_len = 0
        now_sub_palStr = ""
        # 针对回文的中心点为单个字符时
        length = len(s)
        for i in range(0, length):
            is_Pal = True
            left = i
            right = i
            now_sub_palStr = ""
            while(is_Pal and left >=0 and right + 1 <= length):
                now_sub_palStr = s[left:right+1]
                if isPalindrome(now_sub_palStr):
                    left -= 1
                    right += 1
                else:
                    is_Pal = False
            if is_Pal:
                now_len = len(now_sub_palStr)
                if now_len > max_len:
                    max_len = now_len
                    max_sub_palStr = now_sub_palStr
            else:
                now_len = len(now_sub_palStr) - 2
                if now_len > max_len:
                    max_len = now_len
                    max_sub_palStr = now_sub_palStr[1:-1]


            is_Pal = True
            left = i
            right = i + 1
            now_sub_palStr = ""
            while(is_Pal and left >= 0 and right + 1 <= length):
                now_sub_palStr = s[left:right+1]
                if isPalindrome(now_sub_palStr):
                    left -= 1
                    right += 1
                else:
                    is_Pal = False

            if is_Pal:
                now_len = len(now_sub_palStr)
                if now_len > max_len:
                    max_len = now_len
                    max_sub_palStr = now_sub_palStr
            else:
                now_len = len(now_sub_palStr) - 2
                if now_len > max_len:
                    max_len = now_len
                    max_sub_palStr = now_sub_palStr[1:-1]
        return max_sub_palStr


solution = Solution()
res = solution.longestPalindrome("bb")
print(res)