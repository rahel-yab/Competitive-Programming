# Problem: Skibidus and Fanum Tax (hard version) - http://codeforces.com/problemset/problem/2065/C2

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
    n , m = mi()
    a = li()
    b = li()
    b.sort()

    flag = True
    a[0] = min(a[0], b[0] - a[0])
    for i in range(1, n):
        low, high = 0, m-1
        ans = a[i] if a[i] >= a[i-1] else None
        while low<=high:
            mid = (low+high)//2
            diff = b[mid] - a[i]
            if diff >= a[i-1]:
                if ans == None:
                    ans = diff
                else:
                    ans = min(ans, diff)
                high = mid-1
            else:
                low = mid+1
                
        if ans == None:
            flag = False
            break
        a[i] = ans
        
    if flag:
        print("YES")
    else:
        print("NO")

    

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

