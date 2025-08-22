# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = {emp.id:emp for emp in employees}
        # print(graph[1])
        visited = set()
        tot = 0
        def dfs(i):
            nonlocal tot
            visited.add(i.id)
            imp = i.importance
            tot += imp
            sub = i.subordinates
            for nei in sub:
                if nei not in visited:
                    dfs(graph[nei])
        dfs(graph[id])
        return tot

        