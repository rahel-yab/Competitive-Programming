# Problem: 01 Knapsack - https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1

class Solution:
    def knapsack(self, W, val, wt):
        # code here
        memo = [[-1]*(W+1) for _ in range(len(val))]
        def dp(i, weight):
            
                
            if i == len(wt):
                return 0
                
            if memo[i][weight] != -1:
                return memo[i][weight]
            
            not_pick = dp(i+1, weight)
            pick = 0
            if weight + wt[i] <= W:
                pick = val[i] + dp(i+1, weight+wt[i])
            
        
            memo[i][weight] = max(pick, not_pick)
            return memo[i][weight]
            
        
        return dp(0,0)
        
            
