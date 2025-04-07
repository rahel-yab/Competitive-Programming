# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) == 0 and n== 1:
            return 1
        in_deg = [0] * (n+1)
        out_deg = [0] * (n+1)
        for u,v in trust:
            out_deg[u] += 1
            in_deg[v] += 1
        for i in range(1,n+1):
            if in_deg[i] == n-1 and out_deg[i] == 0:
                return i
        return -1