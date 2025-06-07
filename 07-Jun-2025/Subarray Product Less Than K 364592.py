# Problem: Subarray Product Less Than K - https://leetcode.com/problems/subarray-product-less-than-k/

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        count, left , prod = 0 , 0 , 1
        for right in range(len(nums)):
            prod *= nums[right]
            while prod >= k and left < len(nums):
                prod //= nums[left]
                left += 1
            count += right - left + 1
        return count
