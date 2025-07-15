# Problem: Array Elimination - https://codeforces.com/contest/1601/problem/A

import math
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

def solve():
    n = ii()
    arr = li()
    c1 = Counter(arr)
    if c1[0] == n:
        print(*[i for i in range(1,n+1)])
        return
    width = max(arr).bit_length()
    curr = [format(n, f'0{width}b') for n in arr]
    col = list(zip(*curr))
    count = [c.count('1') for c in col]

    gcd = count[0]
    for c in count[1:]:
        gcd = math.gcd(gcd , c)
    # print(gcd)
    ans = []
    for i in range(1,gcd+1):
        if gcd % i == 0:
            ans.append(i)
    print(*ans)


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
#   main_thread = threading.Thread(target=main)
#   main_thread.start()
#   main_thread.join()
