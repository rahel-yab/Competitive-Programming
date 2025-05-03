# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {i:i for i in range(len(edges) + 1)}
        Rank = [0 for i in range(len(edges) + 1)]

        def find(x):
            if graph[x] != x:
                graph[x] = find(graph[x])
            return graph[x]
        
        def union(x,y):
            rootx = find(x)
            rooty = find(y)
            if rootx != rooty:
                if Rank[rootx] > Rank[rooty]:
                    graph[rooty] = rootx
                elif Rank[rooty] > Rank[rootx]:
                    graph[rootx] = rooty  
                else:
                    graph[rootx] = rooty
                    Rank[rooty] += 1 

        def connected(x, y):
            return find(x) == find(y)

        ans = []
        for x,y in edges:
            if connected(x,y):
                ans.append([x,y])
            else:
                union(x,y)

        return ans[-1]         


        