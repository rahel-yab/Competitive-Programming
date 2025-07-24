# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        ans = float("-inf")
        n = len(nums)
        graph = [[] for i in range(n)]
        for i in range(n):
            for j in range(i+2,n):
                graph[i].append(j)
        
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            maxx = 0
            for nei in graph[i]:
                maxx = max (maxx, dfs(nei))
            memo[i] = nums[i] + maxx
            return memo[i]
        return max(dfs(i) for i in range(n))


    