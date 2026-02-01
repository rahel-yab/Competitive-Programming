class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        val = nums.pop(0)
        nums.sort()
        val2 = sum(nums[:2])
        return val + val2