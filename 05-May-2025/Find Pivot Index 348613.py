# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/description/

class Solution(object):
  def pivotIndex(self, nums):
    n = len(nums)
    prefix = [0] * (n+1)
    for i in range(1,n+1):
        prefix[i] = prefix[i-1] + nums[i-1]
    
    for i in range(n):
        pre = prefix[i-n-1]
        suff = prefix[-1] - prefix[i+1]
        if pre == suff:
            return i
    return -1
    
