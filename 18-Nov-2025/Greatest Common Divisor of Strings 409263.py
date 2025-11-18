# Problem: Greatest Common Divisor of Strings - https://leetcode.com/problems/greatest-common-divisor-of-strings/

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        ans = -1

        i = 0
        while i < min(len(str1), len(str2)):
            if str1[i] == str2[i] and len(str1)%(i+1)== 0 and len(str2) % (i+1) == 0:
                ans = i
                i += 1             
            elif str1[i] != str2[i]:
                break
            elif str1[i] == str2[i] and (len(str1)%(i+1)!= 0 or len(str2) % (i+1) != 0):
                i += 1 

        if ans == -1:
            return ""
        
        val = str1[:ans+ 1]
        c = len(val)
        for i in range(c , len(str1), c):
            if str1[i:i+c] != val:
                return ""
        
        for i in range(c , len(str2), c):
            if str2[i:i+c] != val:
                return ""


        return val