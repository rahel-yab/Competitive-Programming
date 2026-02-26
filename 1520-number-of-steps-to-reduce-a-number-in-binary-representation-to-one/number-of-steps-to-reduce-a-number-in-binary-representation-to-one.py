class Solution:
    def numSteps(self, s: str) -> int:
        ans, num , c = 0 , 0 , 1
        for i in range(len(s)-1 , -1 , -1):
            if s[i] == '1':
                num += c
            c *= 2
        while num:
            if num == 1:
                return ans 
            elif num % 2:
                num += 1
            else:
                num //= 2
            ans += 1

