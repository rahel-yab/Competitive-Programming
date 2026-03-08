class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = []
        def backtrack(curr):
            if len(curr) > len(nums[0]):
                return
            if len(curr) == len(nums[0]):
                res.append(curr)
                return
            
            backtrack(curr +'0')
            backtrack(curr +'1')

        backtrack('')

        for binary in res:
            if binary not in nums:
                return binary