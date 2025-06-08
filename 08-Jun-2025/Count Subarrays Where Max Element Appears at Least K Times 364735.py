# Problem: Count Subarrays Where Max Element Appears at Least K Times - https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxx = max(nums)
        ans = start = curr = 0

        for end in range(len(nums)):
            if nums[end] == maxx:
                curr += 1
            while curr == k:
                if nums[start] == maxx:
                    curr -= 1
                start += 1
            ans += start
        return ans