# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ans = 0
        minq = deque()
        maxq = deque()
        left = 0
        for right in range(len(nums)):
            while minq and nums[right] < minq[-1]:
                minq.pop()
            while maxq and nums[right] > maxq[-1]:
                maxq.pop()

            minq.append(nums[right])
            maxq.append(nums[right])
            # print(minq , maxq)

            while maxq[0] - minq[0] > limit:
                if nums[left] == minq[0]:
                    minq.popleft()
                if nums[left] == maxq[0]:
                    maxq.popleft()
                left += 1
            ans = max(ans , right - left + 1)
     
        return ans 
            
