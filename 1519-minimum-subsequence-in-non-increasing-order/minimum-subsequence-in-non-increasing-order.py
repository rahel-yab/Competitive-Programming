class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        while sum(ans) <= sum(nums):
            ans.append(nums.pop())
        return ans