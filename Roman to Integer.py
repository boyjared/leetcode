class Solution:

    def romanToInt(self, s):
        int_num = 0
        RomanRank = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        max_index = 0
        for i in range(len(s)):
            if RomanRank[s[i]] >= RomanRank[s[max_index]]:
                max_index = i
        for i in range(0, max_index):
            int_num = int_num - RomanRank[s[i]]
        for i in range(max_index, len(s)):
            int_num = int_num + RomanRank[s[i]]
        return int_num


solution = Solution()
result = solution.romanToInt("MCMXCVI")
print(result)
