# Problem: The Two Routes - https://codeforces.com/problemset/problem/601/A

from collections import defaultdict
from collections import deque
    
n , m = map(int,input().split())
graph1 = defaultdict(list)
graph2 = defaultdict(list)
sett = set()
for _ in range(m):
    u , v =map(int,input().split())
    sett.add((u,v))
    graph1[u].append(v)
    graph1[v].append(u)


for i in range(1,n+1):
    for j in range(1,n+1):
        if (i,j) not in sett and (j,i) not in sett and i != j:
            graph2[i].append(j)
            graph2[j].append(i)


def bfs(n, graph):
    q = deque()
    q.append([1,0])
    visited = set()
    visited.add(1)
    while q:
        node , l = q.popleft()
        if node == n:
            return l
        for nei in graph[node]:
            if nei not in visited:
                q.append([nei, l+1])
                visited.add(nei)
    
    return -1

val1 , val2 = bfs(n, graph1) , bfs(n , graph2)
if val1 == -1 or val2 == -1:
    print(-1)
else:
    print(max(val1,val2))
