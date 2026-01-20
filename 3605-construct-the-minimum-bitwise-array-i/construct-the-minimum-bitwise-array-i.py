class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        # ans = [float("inf")] * len(nums)
        # for i , num in enumerate(nums):
        #     for x in range(1000):
        #         c = x | (x+1)
        #         if c == num and c  < ans[i]:
        #             ans[i] = x
        # for i in range(len(nums)):
        #     if ans[i] == float("inf"):
        #         ans[i] = -1
        # return ans

        ans = []
        for n in nums:
            if n & 1:
                ans.append(n & ~(((n + 1) & ~n) >> 1))
            else:
                ans.append(-1)
        return ans