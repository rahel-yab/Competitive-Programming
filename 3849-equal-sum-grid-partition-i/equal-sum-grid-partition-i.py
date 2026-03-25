class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        row , col = len(grid) , len(grid[0])

        total = sum(sum(r) for r in grid)
        if total%2:
            return False
        
        target = total // 2
        row_sum = 0
        for r in grid:
            row_sum += sum(r)
            if row_sum == target:
                return True

        col_sum = 0  
        for c in range(col-1):
            
            col_sum += sum(grid[i][c] for i in range(row))
            if col_sum == target:
                return True
        
        return False


