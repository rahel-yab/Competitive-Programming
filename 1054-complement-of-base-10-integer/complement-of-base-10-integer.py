class Solution:
    def bitwiseComplement(self, n: int) -> int:
        ans , c = 0 , 1
        if n == 0:
            return 1
        while n:
            if n & 1 == 0:
                ans += c
            c *= 2
            n >>= 1
        return ans
