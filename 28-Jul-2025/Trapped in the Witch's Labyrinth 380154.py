# Problem: Trapped in the Witch's Labyrinth - https://codeforces.com/problemset/problem/2034/C

from collections import deque
import sys
import threading
 
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def solve(n, m, mat):
    if n == 1 and m == 1:
        print(0)
        return
    def inbound(r, c):
        return 0 <= r < n and 0 <= c < m
    q = deque()
    visited = set()
 
    for r in range(n):
        for c in range(m):
            if (mat[r][c] == 'R' and c == m - 1) or (mat[r][c] == 'L' and c == 0) or (mat[r][c] == 'U' and r == 0) or (mat[r][c] == 'D' and r == n - 1):
                q.append((r, c))
                visited.add((r, c))
    def check(r, c):
        for dr, dc in directions:
            x, y = r + dr, c + dc
            if inbound(x, y) and (x, y) not in visited:
                return
        visited.add((r, c))
        q.append((r, c))
 
    while q:
        r, c = q.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if not inbound(nr, nc) or (nr, nc) in visited:
                continue
            ch = mat[nr][nc]
            if (ch == 'R' and nc == c - 1 and r == nr) or (ch == 'L' and nc == c + 1 and r == nr) or (ch == 'U' and nr == r + 1 and c == nc) or (ch == 'D' and nr == r - 1 and c == nc):
                q.append((nr, nc))
                visited.add((nr, nc))
            if ch == '?':
                check(nr, nc)
    print(n*m - len(visited))
 
def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx + 1])
        idx += 2
        mat = [list(data[idx + i]) for i in range(n)]
        idx += n
        solve(n, m, mat)
 
if __name__ == '__main__':
    sys.setrecursionlimit(1 << 25)
    threading.stack_size(1 << 27)
    thread = threading.Thread(target=main)
    thread.start()
    thread.join()