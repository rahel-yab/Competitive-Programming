# Problem: Fox And Snake - https://codeforces.com/problemset/problem/510/A

n , k = map(int, input().split())
mat = [['.'] * k for _ in range(n)]
left = 1
left2 = 3
for i in range(n):
    for j in range(k):
        if i % 2 == 0:
            mat[i][j] = "#"
        else:
            if i == left:
                if j == k-1:
                    mat[i][j] = '#'
                    left += 4
            if i == left2:
                if j == 0:
                    mat[i][j] = '#'
                    left2 += 4
for row in mat:
    print("".join(row))