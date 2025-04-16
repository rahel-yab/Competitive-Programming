# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        row = len(board)
        col = len(board[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def inbound(r,c):
            if 0 <= r < row and 0<= c < col:
                return True
            return False

        def dfs(r,c):
            if not inbound(r,c) or board[r][c] != 'O':
                return
            board[r][c] = 'V'
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                dfs(nr, nc)

        for r in range(row):
            for c in range(col):
                if board[r][c] == 'O':
                    if r == 0 or (r == row-1) or c == 0 or c ==(col-1):
                        dfs(r,c)
        
        for r in range(row):
            for c in range(col):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
        
        for r in range(row):
            for c in range(col):
                if board[r][c] == 'V':
                    board[r][c] = 'O'
