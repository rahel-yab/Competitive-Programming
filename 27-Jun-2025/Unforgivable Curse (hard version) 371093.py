# Problem: Unforgivable Curse (hard version) - https://codeforces.com/contest/1800/problem/E2

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
    n , k = mi()
    s = si()
    t = si()
    visited = set()
    graph = [[] for _ in range(n)]
    for i in range(n):
        for d in [k, k+1]:
            if i + d < n:
                graph[i].append(i + d)
                graph[i + d].append(i)
    def dfs(i, curr):
        visited.add(i)
        curr.append(i)
        for nei in graph[i]:
            if nei not in visited:
                dfs(nei, curr)

    for i in range(n):
        if i not in visited:
            curr = []
            dfs(i, curr)
            if sorted(s[j] for j in curr) != sorted(t[j] for j in curr):
                print("NO")
                return
    print("YES")

    return

# =========================================
def main():
    t = ii()
    for _ in range(t):
        solve()

if __name__ == '__main__':
    sys.setrecursionlimit(1 << 25)
    threading.stack_size(1 << 27)
    thread = threading.Thread(target=main)
    thread.start()
    thread.join()