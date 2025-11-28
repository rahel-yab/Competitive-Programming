class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        val = max(nums)
        for num in nums:
            if 2*num > val and num!=val:
                return -1

        return nums.index(val)