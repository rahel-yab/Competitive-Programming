# Problem: Thearte Square - https://codeforces.com/problemset/problem/1/A

import math
n , m , k = map(int, input().split())
print(math.ceil(n/k) * math.ceil(m/k))