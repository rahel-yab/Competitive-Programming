# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = defaultdict(list)
        blue = defaultdict(list)
        for u,v in redEdges:
            red[u].append(v)
        for u,v in blueEdges:
            blue[u].append(v)
        
        visited = set()
        visited.add((0,None))
        q = deque()
        q.append([0,0,None])

        ans = [-1 for _ in range(n)]
        while q:
            node, length, color = q.popleft()
            if ans[node] == -1:
                ans[node] = length
            
            if color != 'red':
                for neigh in red[node]:
                    if (neigh,'red') not in visited:
                        q.append([neigh,length+1,'red'])
                        visited.add((neigh,'red'))
            if color != 'blue':
                for neigh in blue[node]:
                    if (neigh,'blue') not in visited:
                        q.append([neigh,length+1,'blue'])
                        visited.add((neigh,'blue'))
        return ans
            
                    
