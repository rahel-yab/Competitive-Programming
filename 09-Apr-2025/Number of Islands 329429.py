# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        directions = [(0,-1) , (0,1), (1,0), (-1,0)]
        ans = 0
        row = len(grid)
        col = len(grid[0])
        def inbound(r,c):
            if 0 <= r < row and 0 <= c < col:
                return True
            return False

        def dfs(r,c):
            visited.add((r,c))
            for dr , dc in directions:
                nr = r + dr
                nc = c + dc
                if inbound(nr,nc) and (nr,nc) not in visited and grid[nr][nc] == '1':
                    dfs(nr,nc)
            return None
    

            
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1' and (r,c) not in visited:
                    dfs(r,c)
                    ans += 1
        return ans
