# Problem: Limited Repainting - https://codeforces.com/contest/2070/problem/C

import math
from math import gcd
import sys, threading
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush
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
# =========================================

"""
# Note

"""

def solve():
    n , k = mi()
    s = si()
    a = li()
    def validate(mid):
        c = 0
        last = 'R'
        for i in range(n):
            if a[i] > mid:
                if s[i] == 'B' and last == 'R':
                    c += 1
                last = s[i]
        return c <= k

    low = 0
    high = max(a)
    while low <= high:
        mid = (low + high)//2
        if validate(mid):
            high = mid -1
        else:
            low = mid + 1
    print(low)


# =========================================
def main():
    t = ii()
    for _ in range(t):
        solve()

# =========================================
main()
# if __name__ == '__main__':
#   sys.setrecursionlimit(1 << 30)
#   threading.stack_size(1 << 27)
#   main_thread = threading.Thre ad(target=main)
#   main_thread.start()
#   main_thread.join()