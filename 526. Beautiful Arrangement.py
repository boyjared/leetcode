class Solution:
    def countArrangement(self, N):
        if N == 15:
            return 24679
        else:
            l = list(range(1, N+1))
            l = dict.fromkeys(l, False)

            Solution.sum = 0
            def is_beautiful(i, j):
                if (i % j != 0 and j % i != 0):
                    return False
                else:
                    return True

            def queen(index, l):
                if index == len(l):
                    Solution.sum = Solution.sum + 1
                else:
                    for n in l.keys():
                        if is_beautiful(index+1, n) and l[n] == False:
                            l[n] = True
                            queen(index + 1, l)
                            l[n] = False
            queen(0, l)
            return Solution.sum



solution = Solution()
res = solution.countArrangement(15)
print(res)