# Problem: Single Number - https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        val = 0
        for i in range(len(nums)):
            val ^= nums[i] 
        return val