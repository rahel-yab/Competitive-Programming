# Problem: Count Subarrays With Fixed Bounds - https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0
        start, end = -1, -1
        left = -1

        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                left = i 
            if num == minK:
                start = i
            if num == maxK:
                end = i
            if start >= left and end >= left:
                count += min(start, end) - left

        return count