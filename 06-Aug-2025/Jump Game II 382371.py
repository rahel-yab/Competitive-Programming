# Problem: Jump Game II - https://leetcode.com/problems/jump-game-ii/description/

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def dfs(i):
            if i == n - 1:
                return 0
            if i in memo:
                return memo[i]

            ans = float('inf')
            for j in range(1, nums[i] + 1):
                curr = i + j
                if curr < n: 
                    ans = min(ans, 1 + dfs(curr))
            memo[i] = ans
            return memo[i]

        return dfs(0)