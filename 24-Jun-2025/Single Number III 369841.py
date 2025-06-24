# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        
        c = 0
        while xor >> c  & 1 != 1:
            c += 1

        g , t = 0 ,0
        for num in nums:
            if 1 & num >> c:
                g ^= num
            else:
                t ^= num
        return [g,t]