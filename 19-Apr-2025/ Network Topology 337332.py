# Problem:  Network Topology - https://codeforces.com/problemset/problem/292/B

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
    n, m = mi()
    graph = [[] for _ in range(n+1)]
    
    
    for _ in range(m):
        i,j = mi()
        graph[i].append(j)
        graph[j].append(i)

    one = 0
    two = 0
    star = 0
    for j in range(1,n+1):
        length = len(graph[j])
        if length == 1:
           one += 1
        if length == 2:
            two += 1
        if length == n-1:
            star += 1
   
   
    if one == 2 and two == n-2:
        print('bus topology')
    elif two == n:
        print('ring topology')
    elif one == n-1 and star == 1:
        print('star topology')
    else:
        print('unknown topology')
    

        

# =========================================
def main():
    t = 1
    for _ in range(t):
        solve()

# =========================================
main()
# if __name__ == '__main__':
#   sys.setrecursionlimit(1 << 30)
#   threading.stack_size(1 << 27)
#   main_thread = threading.Thread(target=main)
#   main_thread.start()
#   main_thread.join()