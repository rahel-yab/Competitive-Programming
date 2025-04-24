# Problem: Count complete subarrays in an array - https://leetcode.com/problems/count-complete-subarrays-in-an-array/

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        left = 0
        count = 0
        c = set(nums)
        length = len(c)
        dictt = {}
        for right in range(len(nums)):
            if nums[right] in dictt:
                dictt[nums[right]] += 1
            else:
                dictt[nums[right]] = 1

            while len(dictt) == length:
                count += len(nums)- right
                dictt[nums[left]] -= 1
                if dictt[nums[left]] == 0:
                    del dictt[nums[left]]
                left += 1
        return count
