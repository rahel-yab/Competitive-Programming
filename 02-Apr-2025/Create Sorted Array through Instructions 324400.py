# Problem: Create Sorted Array through Instructions - https://leetcode.com/problems/create-sorted-array-through-instructions/

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:

        total = 0
        res = []
        mod = 10 **9 + 7
        for num in instructions:
            ind = bisect_left(res, num)
            right = bisect_right(res,num)
            total += min(len(res)-right,ind)
            res.insert(right,num)
            
        return total % mod
        
