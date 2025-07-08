# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A

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
    mat = []
    for _ in range(5):
        l = li()
        mat.append(l)
    flag = False
    for r in range(5):
        for c in range(5):
            if mat[r][c] == 1:
                flag = True
                break
        if flag:
            break
    print(abs(2-r) + abs(2-c))
    
    
# =========================================
def main():
    t = 1
    for _ in range(t):
        solve()
main()

# if __name__ == '__main__':
#     sys.setrecursionlimit(1 << 25)
#     threading.stack_size(1 << 27)
#     thread = threading.Thread(target=main)
#     thread.start()
#     thread.join()