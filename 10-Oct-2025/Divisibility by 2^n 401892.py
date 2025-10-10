# Problem: Divisibility by 2^n - https://codeforces.com/contest/1744/problem/D

import math
import random
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
    n = ii()
    arr = li()
    def counts(x):
        c = 0 
        while not x & 1:
            x >>= 1
            c += 1
        return c

    summ = 0
    for num in arr:
        summ += counts(num)

    rem = n-summ
    if rem <= 0:
        print(0)
        return

    curr = sorted([counts(i) for i in range(2, n+1, 2)], reverse = True)
    if sum(curr) < rem:
        print(-1)
        return
    
    count = 0
    gain = 0 
    for i in curr:
        gain += i
        count += 1
        if gain >= rem:
            print(count)
            return
    print(-1)
      

    return
# =========================================
def main():
    t = ii()
    for _ in range(t):
        solve()
main()

# if __name__ == '__main__':
#     sys.setrecursionlimit(1 << 25)
#     threading.stack_size(1 << 27)
#     thread = threading.Thread(target=main)
#     thread.start()
#     thread.join()
