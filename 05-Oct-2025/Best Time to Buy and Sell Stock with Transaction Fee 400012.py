# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        memo = {}
        def dp(i, prev):

            if i >= len(prices):
                return 0

            state = (i, prev)
            if state in memo:
                return memo[state]


            sell , buy = 0 ,0
            if prev == 'buy':
                sell = prices[i] + dp(i+1, 'sell') - fee
                
            skip = dp(i+1, prev)
            buy = dp(i+1, 'buy') - prices[i]

            memo[state] = max(skip, buy , sell)
            return memo[state]

        
        return max(dp(0, 'buy') - prices[0], 0, dp(0 , 'skip'))