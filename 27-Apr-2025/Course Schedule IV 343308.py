# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        n = numCourses
        graph = [[] for _ in range(n)]
        
        for u,v in prerequisites:
            graph[v].append(u)
        
        def bfs(s,e):
            q = deque()
            q.append(s)
            visited = set()
            while q:
                node = q.popleft()
                visited.add(node)
                if node == e:
                    return True
                for nei in graph[node]:
                    if nei not in visited:
                        q.append(nei)

            return False
        
        res = []
        for u,v in queries:
            res.append(bfs(v,u))
        return res
        