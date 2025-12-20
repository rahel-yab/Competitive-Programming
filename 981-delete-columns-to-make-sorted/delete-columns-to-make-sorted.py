class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        new_strs = []
        for i in range(len(strs[0])):
            w = []
            for j in strs:
                w.append(j[i])
            new_strs.append(''.join(w))
        
        ans = 0
        for word in new_strs:
            if word != ''.join(sorted(word)):
                ans += 1
        return ans
