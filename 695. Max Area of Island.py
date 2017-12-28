class Solution:
    def maxAreaOfIsland(self, grid):
        seen = set()
        max_island = 0
        def area(r, c):
            if (r, c) not in seen and 0 <= r < len(grid) and 0 <=c < len(grid[0]) and grid[r][c]:
                seen.add((r, c))
                return (1 + area(r+1,c) + area(r-1,c) + area(r, c+1) + area(r, c-1))
            else:
                return 0
        for r in range(0,len(grid)):
            for c in range(0, len(grid[0])):
                result = area(r,c)
                if result > max_island:
                    max_island = result
        return max_island
