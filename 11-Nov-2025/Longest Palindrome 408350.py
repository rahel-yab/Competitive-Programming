# Problem: Longest Palindrome - https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)

        ans = 0
        k = 1
        for key , val in c.items():
            rem = val % 2
            if rem == 0:
                ans += val
                c[key] = 0
            else:
                ans += val -1
                c[key] = 1
        
        
        for key , val in c.items():
            if val == 1:
                ans += 1
                break
        
        return ans


