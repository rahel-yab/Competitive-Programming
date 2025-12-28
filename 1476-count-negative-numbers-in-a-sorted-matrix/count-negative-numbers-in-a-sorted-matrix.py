class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans  = 0 
        row , col = len(grid) , len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] < 0:
                    ans += 1
        return ans