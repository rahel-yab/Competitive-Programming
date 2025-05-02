# Problem: Minimum Operations to Exceed Threshold Value II - https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        count = 0 
        while len(nums) >= 2:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            if x < k or y < k:
                val = (min(x, y) * 2 + max(x, y))
                heapq.heappush(nums,val)
                count += 1
        return count
