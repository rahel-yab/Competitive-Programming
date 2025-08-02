# Problem: Find the Power of K-Size Subarrays II - https://leetcode.com/problems/find-the-power-of-k-size-subarrays-ii/

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        left = 0
        right = 0 
        
        count = 0
        ans = [-1] * (n -k+1)
        while right < n :
            if right > 0 and nums[right] == nums[right-1] +1:
                count += 1
            else:
                count = 0
                left = right

            if right - left + 1 == k and count == k-1:
                ans[left] = nums[right]
                left += 1
                count -= 1
            right += 1
         
        return ans


            