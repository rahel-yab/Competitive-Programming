# Problem: Sereja and Dima - https://codeforces.com/problemset/problem/381/A

n = int(input())
arr = list(map(int, input().split()))
left = 0
right = n - 1
s = 0  
d = 0  
c = 0 

while left <= right:
    if arr[right] > arr[left]:
        curr = arr[right]
        right -= 1
    else:
        curr = arr[left]
        left += 1

    if c % 2 == 0:
        s += curr 
    else:
        d += curr  

    c += 1

print(s, d)
