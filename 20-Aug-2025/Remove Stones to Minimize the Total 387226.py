# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        for i in piles:
            heappush(heap, -i)
        
        while k and heap:
            val = -(heappop(heap))
            curr = ceil(val/2)
            heappush(heap ,-curr)
            k-= 1
        return -sum(heap)