# Problem: A - Frog 1 - https://atcoder.jp/contests/dp/tasks/dp_a

n = int(input())
arr = list(map(int, input().split()))
dp = [float("inf")] * n
dp[0] = 0
dp[1] = abs(arr[0] -arr[1])
for j in range(2,n):
    dp[j] = min(abs(arr[j] - arr[j-1])+dp[j-1] , abs(arr[j-2] - arr[j])+dp[j-2])

# print(dp)
print(dp[-1])