# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        dp = [[0] *(i+1) for i in range(len(triangle))]
        dp[0][0] = triangle[0][0]

        def inbound(r,c):
            return 0 <= r < len(triangle) and 0<= c <= r
        
        for r in range(len(triangle)):
            for c in range(r+1):
                if r== 0 and c == 0:
                    continue
                
                up , left = float("inf") , float("inf")
                if inbound(r-1,c):
                    up = triangle[r][c] + dp[r-1][c]
                if inbound(r-1,c-1):
                    left = triangle[r][c] + dp[r-1][c-1]
                dp[r][c] = min(up, left)
        # print(dp)
        return min(dp[-1])
       