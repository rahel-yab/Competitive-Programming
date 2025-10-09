# Problem: Complicated GCD - https://codeforces.com/contest/664/problem/A

import math
a,b = map(int,input().split())
minn = float('inf')
if a == b:
    print(a)
else:
    print(1)