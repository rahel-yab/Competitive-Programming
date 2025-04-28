# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        right = (n-1) %2
        cell = 1
        mapp = {}
        for row in range(n-1,-1,-1):
            curr = row %2
            if curr == right:
                for col in range(n):
                    mapp[cell] = (row,col)
                    cell += 1

            else:
                for col in range(n-1,-1,-1):
                    mapp[cell] = (row,col)
                    cell += 1
        target = n **2
        q = deque([1])
        visited = set([1])
        level = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                row,col = mapp[node]
                if board[row][col] != -1:
                    node = board[row][col]
                if node == target:
                    return level
                for add in range(1,7):
                    if node + add > target:
                        break
                    neigh = node + add
                    if neigh not in visited:
                        q.append(neigh)
                        visited.add(neigh)
            level += 1
                    


        
        return -1


        