class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left , right = 0 , 1
        while right < len(nums) and left < len(nums):
            if nums[left] % 2 == 1 and nums[right] % 2 == 0:
                nums[left] , nums[right] = nums[right] , nums[left]
                left += 1
            if (nums[left]%2 == 0 and nums[right]%2 == 1):
                left += 1
            if (nums[left]%2 == 0 and nums[right]%2 == 0):
                left += 2
                right = left

            right += 1
        
        return nums