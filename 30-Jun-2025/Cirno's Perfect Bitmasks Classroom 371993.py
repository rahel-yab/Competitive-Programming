# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

t = int(input())
for _ in range(t):
    x = int(input())
    # print( 1000000 & -1000000)
    y = x & -x
    while x ^ y == 0 or x & y == 0:
        y += 1
    print(y)