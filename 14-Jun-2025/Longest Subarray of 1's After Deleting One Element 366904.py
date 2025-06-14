# Problem: Longest Subarray of 1's After Deleting One Element - https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, k , maxx = 0 , 0 , 0
        for right in range(len(nums)):
            if nums[right] == 0:
                k += 1
            while k > 1:
                if nums[left] == 0:
                    k -= 1
                left += 1        
            maxx = max(maxx, right -left)
        return maxx
      