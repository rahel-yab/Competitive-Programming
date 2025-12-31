class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        curr = []
        ans.add(tuple(curr))
        def backtrack(i):
            if i >= len(nums) or len(curr) > len(nums):
                return
            
            curr.append(nums[i])
            ans.add(tuple(sorted(curr[:])))
            
            backtrack(i+1)
            curr.pop()
            backtrack(i+1)
        
        backtrack(0)
        return list(ans)
