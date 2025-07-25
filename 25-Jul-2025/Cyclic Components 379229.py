# Problem: Cyclic Components - https://codeforces.com/problemset/problem/977/E

import math
import heapq
import sys, threading
from bisect import bisect_left, bisect_right
from collections import defaultdict, Counter, deque

input = lambda: sys.stdin.readline().rstrip()
def si():
    return input()
def ii():
    return int(input())
def lsi():
    return input().split()
def mi():
    return map(int, input().split())
def li():
    return list(map(int, input().split()))
yn = lambda condition: 'YES' if condition else 'NO'

# ========================================
# =========================================
def solve():
    n , e = mi()
    graph = [[] for _ in range(n+1)]
    if n < 3:
        print(0)
        return
    for _ in range(e):
        u, v = mi()
        graph[u].append(v)
        graph[v].append(u)
    
    visited = set()
    def dfs(i, node):
        visited.add(i)
        nonlocal flag
        nonlocal connected
        if len(graph[i]) != 2:
            flag = False
        for nei in graph[i]:
            if nei == node and nei != i:
                connected = True
            if nei not in visited:
                dfs(nei, node)
    
    ans = 0
    for i in range(1,n+1):
        if i not in visited:
            flag = True
            connected = False
            dfs(i, i)
            if flag and connected:
                ans += 1

    print(ans)



    return
# =========================================
def main():
    t = 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    sys.setrecursionlimit(1 << 25)
    threading.stack_size(1 << 27)
    thread = threading.Thread(target=main)
    thread.start()
    thread.join()



