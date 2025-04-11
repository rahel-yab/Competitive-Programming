# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0,-1),(0,1),(1,0),(-1,0)]
        row = len(grid)
        col = len(grid[0])
        visited = []
        ans = 0
        def inbound(r,c):
            if 0 <= r < row and 0 <= c < col:
                return True
            return False
        def dfs(r,c):
            nonlocal ans
            visited.append((r,c))
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if inbound(nr,nc) and grid[nr][nc] == 1 and (nr,nc) not in visited:
                    dfs(nr,nc)
                elif not inbound(nr,nc):
                    ans += 1
                elif grid[nr][nc] == 0:
                    ans += 1
            return ans
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    return dfs(r,c)
