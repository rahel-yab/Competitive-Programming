class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:

        curr  , ans = 1 , 1
       
        for right in range(1 ,len(prices)):
            diff = prices[right-1] - prices[right]
            if  diff == 1:
                curr += 1
            else:
                curr = 1
            ans += curr
        

        return ans


     
        

