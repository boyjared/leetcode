class Solution:
    def checkRecord(self, s):
        if "LLL" in s:
            return False
        if len(s) > 1 and sorted(s)[1] == "A":
            return False
        return True

solution = Solution()
record = "AAAA"
result = solution.checkRecord(record)
print(result)

