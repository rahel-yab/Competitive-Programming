# Problem: Repeated DNA Sequences - https://leetcode.com/problems/repeated-dna-sequences/

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seq = {}
        res = []
        if len(s) <= 10:
            return res
        for i in range(len(s)-9):
            if s[i:i+10] in seq:
                seq[s[i:i+10]] += 1
            else:
                seq[s[i:i+10]] = 1
        
        for key, val in seq.items():
            if val > 1:
                res.append(key)
        return res