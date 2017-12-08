class Solution:
    def detectCapitalUse(self, word):
        length_word = len(word)
        if word[0]>='a' and word[0]<='z':
            for i in range(1, length_word):
                if word[i]>='A' and word[i]<='Z':
                    return False
            return True
        if word[0]>='A' and word[0]<='Z':
            if word.capitalize() == word:
                return True
            elif sorted(word)[-1] >= 'a' and sorted(word)[-1] <= 'z':
                return False
            return True

solution = Solution()
word = "FlaG"
result = solution.detectCapitalUse(word)
print(result)

