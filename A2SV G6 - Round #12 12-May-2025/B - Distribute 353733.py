# Problem: B - Distribute - https://codeforces.com/gym/606404/problem/B

n = int(input())
nums = list(map(int, input().split()))
new = sorted(nums)
mapp = {}
for i in range(n):
    if nums[i] in mapp:
        mapp[nums[i]].append(i)
    else:
        mapp[nums[i]] = [i]

left = 0
right = n - 1
pair = []

while left < right:
    pair.append((new[left], new[right]))
    left += 1
    right -= 1
for u, v in pair:
    print(mapp[u].pop() + 1, mapp[v].pop() + 1)