class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        left , right , ans = 0 , 1 , 0
        for i in range(1 , len(s)):
            if s[i] != s[i-1]:
                ans += min(left , right)
                left , right = right , 1
            else:
                right += 1
        
        return ans + min(left , right)

