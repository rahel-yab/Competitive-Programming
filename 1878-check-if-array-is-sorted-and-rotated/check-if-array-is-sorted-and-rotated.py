class Solution:
    def check(self, nums: List[int]) -> bool:
        cnt = 0
        for i in range(len(nums)):
            if nums[i] < nums[i-1]:
                cnt += 1
      
        return True if cnt <= 1 else False
        