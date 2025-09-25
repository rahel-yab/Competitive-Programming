# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[0] != 0 or stones[1] != 1:
            return False

        sett = set(stones)
        memo = {}
        def dp(i, k):
            state = (i,k)
            if state in memo:
                return memo[state]

            if i == stones[-1]:
                return True

            for j in range(k-1,k+2):
                if i + j in sett and j > 0:
                    if dp(i + j,j):
                        memo[state] = True
                        return True
            
            memo[state] = False
            return memo[state]
        
        return dp(1,1)
        