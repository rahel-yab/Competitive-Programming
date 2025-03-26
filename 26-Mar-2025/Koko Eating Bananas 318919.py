# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isCapacity(k):
            hour = 0
            for i in piles:
                hour += math.ceil(i/k)
            return hour <= h

        low = 1
        high = max(piles)
        while low <= high:
            mid = (low + high)//2
            if isCapacity(mid):
                high = mid -1
            else:
                low = mid + 1
        return low