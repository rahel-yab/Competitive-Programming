class Solution:
    def binaryGap(self, n: int) -> int:
        prev , curr , ans , cnt  = 0 , 0, 0 , 0

        i = 0
        while n:
            if n & 1:
                prev , curr = curr , i
                cnt += 1
            if cnt > 1:
                ans = max(ans , curr - prev)
            n >>= 1
            i += 1
        return ans
