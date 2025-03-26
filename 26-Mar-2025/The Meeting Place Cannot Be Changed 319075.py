# Problem: The Meeting Place Cannot Be Changed - https://codeforces.com/problemset/problem/780/B

n = int(input())
x = list(map(int, input().split()))
v = list(map(int, input().split()))


def yigerem(time):
    max_left = float('-inf')
    min_right = float('inf')
    for xi, vi in zip(x,v):
        displacement = vi * time
        left = xi - displacement
        right = xi + displacement
        max_left = max(max_left,left)
        min_right = min(min_right, right)
    

    return max_left <= min_right


low = 0
high = max(x) - min(x)
precision = 10 ** -6
while low <= high:
    mid = (low + high) / 2
    if yigerem(mid):
        high = mid - precision
    else:
        low = mid + precision
print(low)