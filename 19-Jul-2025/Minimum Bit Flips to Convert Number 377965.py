# Problem: Minimum Bit Flips to Convert Number - https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        val = start ^ goal
        ans = 0
        while val:
            if val & 1 == 1:
                ans += 1
            val >>= 1
        return ans
