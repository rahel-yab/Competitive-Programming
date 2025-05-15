# Problem: Find Xor-Beauty of Array - https://leetcode.com/problems/find-xor-beauty-of-array/

class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]
        for i in range(1,n):
            res ^= nums[i]
        return res