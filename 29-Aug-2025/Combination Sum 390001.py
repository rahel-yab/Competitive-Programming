# Problem: Combination Sum - https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
            
        res = []

        def backtrack(idx, curr, summ):
            if summ == target:
                res.append(curr[:])
                return
            
            if summ > target or idx >= len(candidates):
                return
            
            curr.append(candidates[idx])
            backtrack(idx, curr, summ + candidates[idx])
            curr.pop()
            backtrack(idx+1, curr, summ)

            return res

        return backtrack(0, [], 0)