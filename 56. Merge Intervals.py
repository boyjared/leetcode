# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        merged_l = []
        sorted_l = sorted(intervals, key=lambda interval : interval[0])
        print(sorted_l)
        for i in sorted_l:
            if merged_l == []:
                merged_l.append(i)
            elif i[0] > merged_l[-1][1]:
                merged_l.append(i)
            elif merged_l[-1][1] < i[1]:
                merged_l[-1][1] = i[1]
            else:
                continue
            # print(merged_l)
        return merged_l

solution = Solution()
result = solution.merge([[1,3],[2,6],[8,10],[15,18]])
print(result)
