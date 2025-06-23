# Problem: Longest Increasing Path in a Matrix - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        directions = [(0,1), (0,-1), (1,0),(-1,0)]
        def inbound(r,c):
            return 0 <= r < row and 0 <= c < col

        maxx = float('-inf')
        visited = set()
        mapp = [[None for _ in range(col)] for _ in range(row)]
        def dfs(r,c):
            ans = 1
            # visited.add((r,c))
            if mapp[r][c]:
                return mapp[r][c]
            for dr , dc in directions:
                nr = r + dr
                nc = c + dc
                if inbound(nr,nc) and (nr,nc) not in visited and matrix[nr][nc] > matrix[r][c]:
                    ans = max(ans, 1 + dfs(nr, nc))
            mapp[r][c] = ans  
            return ans


        for r in range(row):
            for c in range(col):
                maxx = max(maxx , dfs(r,c))
        return maxx