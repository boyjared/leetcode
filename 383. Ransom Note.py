class Solution:
    def sortString(self, s):
        l = list(s)
        l.sort()
        s = "".join(l)
        return s
    def string2dict(self, s):
        dict = {}
        for c in s:
            dict.setdefault(c, 0)
            dict[c] = dict[c] + 1
        return dict

    def canConstruct(self, ransomNote, magazine):
        dict_r = self.string2dict(ransomNote)
        dict_m = self.string2dict(magazine)
        for r_key in dict_r.keys():
            if r_key in dict_m.keys() and dict_m[r_key] >= dict_r[r_key]:
                continue
            else:
                return False
        return True

solution = Solution()
result = solution.canConstruct("bg","efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj")
print(result)