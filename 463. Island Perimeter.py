class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        island = 0
        neighbor = 0
        for g in range(len(grid)):
            for x in range(len(grid[g])):
                if grid[g][x] != 0:
                    island = island + 1
                    if g < len(grid)-1 and grid[g+1][x] != 0:
                        neighbor = neighbor + 1
                    if (x < len(grid[g]) -1 and grid[g][x+1] != 0):
                        neighbor = neighbor + 1
        return (island*4-neighbor*2)

solution = Solution()
result = solution.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])
print(result)
