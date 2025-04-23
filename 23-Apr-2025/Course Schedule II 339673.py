# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indeg = [0 for _ in range(numCourses)]

        for u, v in prerequisites:
            graph[v].append(u)
            indeg[u] += 1

        q = deque()
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
        res = []

        while q:
            course = q.popleft()
            res.append(course)

            for neigh in graph[course]:
                indeg[neigh] -= 1
                if indeg[neigh] == 0:
                    q.append(neigh)

        if len(res) != numCourses:
            return []
        return res
