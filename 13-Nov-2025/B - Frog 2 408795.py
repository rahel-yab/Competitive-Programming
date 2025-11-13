# Problem: B - Frog 2 - https://atcoder.jp/contests/dp/tasks/dp_b

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
    h = li()

    dp = [float("inf")] * n
    dp[0] = 0
    for i in range(1 , min(n , k+1)):
        dp[i] = abs(h[0] - h[i])
    for i in range(k+1 , n):
        for j in range(min(k , n-1) , -1 , -1 ):
            dp[i] = min(dp[i] , abs(h[i] - h[i-j])+ dp[i-j])
            
    print(dp[-1])
    # def dp(i):
    #     if i == n - 1:
    #         return 0
    #     ans = float('inf')
    #     for j in range(1, min(k+1, n - i)):
    #         ans = min(ans, abs(h[i] - h[i + j]) + dp(i + j))
    #     return ans

    
    # print(dp(0))
    

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





