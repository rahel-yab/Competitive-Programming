# Problem: Bear and Poker - https://codeforces.com/problemset/problem/574/C

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
    n = ii()
    arr = li()
    for i in range(n):
        while arr[i] %2 == 0:
            arr[i] //= 2
        while arr[i] %3 == 0:
            arr[i] //= 3 
    if len(set(arr)) == 1:
        print('Yes')
    else:
        print('No')
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





