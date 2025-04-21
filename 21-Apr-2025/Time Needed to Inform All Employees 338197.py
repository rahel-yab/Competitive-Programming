# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = [[] for _ in range(n)]
        for i in range(n):
            if manager[i] != -1:
                graph[manager[i]].append(i)

        def dfs(node):
            if not graph[node]:
                return 0
            ans = 0
            for neigh in graph[node]:
                ans = max(ans, dfs(neigh))
            return ans + informTime[node]

        return dfs(headID)

    