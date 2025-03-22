# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        curr =  []

        def backtrack(i):
            if i == n:
                ans.append(curr[:])
                return
            backtrack(i + 1)

            curr.append(nums[i])
            backtrack(i + 1)
            curr.pop()

        backtrack(0)
        return ans
