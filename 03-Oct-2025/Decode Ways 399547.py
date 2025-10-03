# Problem: Decode Ways - https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        
        @cache
        def dp(i):
            if i > len(s):
                return 0
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            one =0
            if 0 <= i < len(s) and 1 <= int(s[i:i+1]) < 27:
                one= dp(i+1)
            two = 0
            if 0 <= i < len(s) and 1 <= int(s[i:i+2]) < 27:
                two = dp(i+2)
            return  one + two
        
        return dp(0)