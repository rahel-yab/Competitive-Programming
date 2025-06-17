# Problem: Longest Happy Prefix - https://leetcode.com/problems/longest-happy-prefix/description/

class Solution:
    def longestPrefix(self, s: str) -> str:
        pre = ""
        suf = ""
        maxx = ""
        for i in range(len(s) - 1):  
            pre += s[i]  
            suf = s[-(i + 1)] + suf  
            if pre == suf: 
                maxx = pre 
                
        return maxx
