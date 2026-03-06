class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        curr = []
        for i in range(len(s)):
            if s[i] == '1':
                curr.append(i)
        
        for i in range(1,len(curr)):
            if curr[i] - curr[i-1] != 1:
                return False
        
        return True