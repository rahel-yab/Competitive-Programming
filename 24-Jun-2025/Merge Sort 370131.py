# Problem: Merge Sort - https://codeforces.com/problemset/problem/873/D

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
# =========================================

def solve():
    n, k = mi()
    if k % 2 == 0:
        print(-1)
        return
    nums = list(range(1, n+1))
    ans = 1
    def merge(l, r):
        nonlocal ans
        if r - l <= 1 or ans == k:
            return
        mid = (l + r) // 2
        nums[mid - 1],nums[mid] =nums[mid],nums[mid - 1] 
        ans += 2 
        merge(l, mid)
        merge(mid, r)

    merge(0, n)
    if ans != k:
        print(-1)
    else:
        print(*nums)

# =========================================
def main():
    t = 1
    for _ in range(t):
        solve()

# =========================================
if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)
    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
