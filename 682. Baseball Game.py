class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        score = []
        sum_score = 0
        for o in ops:
            if o == 'C':
                if len(score) == 0:
                    continue
                else:
                    sum_score = sum_score - score.pop()
            elif o == 'D':
                if len(score) == 0:
                    continue
                else:
                    sum_score = sum_score + score[-1]*2
                    score.append(score[-1]*2)
            elif o == '+':
                if len(score) == 0:
                    continue
                elif len(score) == 1:
                    sum_score = sum_score + score[0]*2
                    score.append(score[0]*2)
                else:
                    sum_score = sum_score + score[-1] + score[-2]
                    score.append(score[-1] + score[-2])
            else:
                score.append(int(o))
                sum_score = sum_score + int(o)
        return sum_score

solution = Solution()
res = solution.calPoints(["5","-2","4","C","D","9","+","+"])
print(res)
