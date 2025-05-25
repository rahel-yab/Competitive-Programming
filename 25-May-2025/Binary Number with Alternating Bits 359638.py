# Problem: Binary Number with Alternating Bits - https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        turn = n & 1
        n >>= 1
        while n:
            if n & 1 == turn:
                return False
            turn = n & 1
            n >>= 1
        return True