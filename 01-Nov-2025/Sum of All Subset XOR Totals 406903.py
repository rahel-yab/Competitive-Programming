# Problem: Sum of All Subset XOR Totals - https://leetcode.com/problems/sum-of-all-subset-xor-totals/

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        @cache
        def backtrack(i, total):
            if i >= len(nums):
                return total
            
            return backtrack(i+1 , total) + backtrack(i+1 , total^nums[i])

        return backtrack(0, 0)
