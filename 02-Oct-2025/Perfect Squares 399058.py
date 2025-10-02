# Problem: Perfect Squares - https://leetcode.com/problems/perfect-squares/

class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i*i for i in range(1, int(n**0.5) + 1)]
        dp = [float('inf')]*(n + 1)
        dp[0] = 1
        for i in range(1,n + 1):
            for num in squares:
                if 0 <= i-num <= n:
                    dp[i] = min(dp[i], 1+dp[i-num])
                    
        return dp[n]-1

        # @cache
        # def dp(i,total):
        #     if i >= int(n**0.5) + 1:
        #         return float('inf')

        #     if total > n:
        #         return float('inf')
            
        #     if total == n:
        #         return 0
            
        #     return min(1 + dp(i,total+(i**2))) , dp(i+1,total))

        # return dp(0,0)