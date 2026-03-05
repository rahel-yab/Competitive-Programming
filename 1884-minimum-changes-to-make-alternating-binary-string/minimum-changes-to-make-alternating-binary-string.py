class Solution:
    def minOperations(self, s: str) -> int:
        s1 = ['0']
        s2 = ['1']
        for i in range(len(s)):
            if s1[-1] == '0':
                s1.append('1')
            if s1[-1] == '1':
                s1.append('0')
            if s2[-1] == '0':
                s2.append('1')
            if s2[-1] == '1':
                s2.append('0')
        
        min1 , min2 = 0 , 0
        for i in range(len(s)):
            if s1[i] != s[i]:
                min1 += 1
            if s2[i] != s[i]:
                min2 += 1
        
        return min(min1 , min2)

 