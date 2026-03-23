from functools import cache

class Solution:
    def maxProductPath(self, grid: list[list[int]]) -> int:
        row, col = len(grid), len(grid[0])
        
        @cache
        def dp(r, c):
            if r == row - 1 and c == col - 1:
                return grid[r][c], grid[r][c]
            
            res_max, res_min = float("-inf"), float("inf")
            
            for nr, nc in [(r + 1, c), (r, c + 1)]:
                if nr < row and nc < col:
                    p_max, p_min = dp(nr, nc)
                    vals = (grid[r][c] * p_max, grid[r][c] * p_min)
                    res_max = max(res_max, max(vals))
                    res_min = min(res_min, min(vals))
            
            return res_max, res_min

        val, _ = dp(0, 0)
        return val % (10**9 + 7) if val > -1 else -1