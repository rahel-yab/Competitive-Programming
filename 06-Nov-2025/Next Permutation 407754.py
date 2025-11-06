# Problem: Next Permutation - https://leetcode.com/problems/next-permutation/description/

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        ind1 , ind2 = -1 , -1
        for i in range(n-2 , -1 , -1):
            if nums[i] < nums[i+1]:
                ind1 = i
                break
        for i in range(n-1 , ind1 , -1):
            if nums[i] > nums[ind1]:
                ind2 = i
                break

        if ind1 == -1 or ind2 == -1:
            nums.sort()
            return
        
        nums[ind1] , nums[ind2] = nums[ind2] , nums[ind1]
        nums[ind1+1:] = reversed(nums[ind1+1:])


