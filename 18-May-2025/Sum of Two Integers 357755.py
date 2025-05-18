# Problem: Sum of Two Integers - https://leetcode.com/problems/sum-of-two-integers/description/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF 
        maxx = 0x7FFFFFFF
        x = a & mask
        y = b & mask
        while y != 0:
            curr = (x&y) << 1
            x = x ^ y
            y = curr & mask
        
        if x <= maxx:
            return x
        else:
            return ~(x^mask)