# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in stones:
            heappush(heap,-i)
        
        while heap:
            if len(heap) == 1:
                return -heappop(heap)
            x = abs(heappop(heap))
            y = abs(heappop(heap))
        
            if x < y:
                heappush(heap, -(y-x))
            elif x > y:
                heappush(heap, -(x-y))

        return 0
