class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans  = 0 
        row , col = len(grid) , len(grid[0])
        for i in range(col-1 , -1 , -1):
            j = 0
            while 0 <= j < row and grid[j][i] >= 0:
                j += 1

            ans += row - j 
        
        return ans