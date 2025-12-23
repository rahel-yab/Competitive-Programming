class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        # TRACK EACH NODE'S RANK AND ITS LOWEST RANK
        rank = [None] * n
        lowest_rank = [None] * n
        
        # CREATE THE GRAPH
        g = self.create_graph(connections)
        
        # DFS FROM NODE 0
        critical = []
        self.dfs(g, 0, None, set(), rank, lowest_rank, critical)
        return critical
        
        
    def dfs(self, g, curr, parent, vis, rank, lowest_rank, critical):
        if curr in vis:
            return
        
        vis.add(curr)
        
        rank[curr] = len(vis)
        lowest_rank[curr] = len(vis)
        
        for nb in g.get(curr, []):
            if nb == parent:
                continue
            self.dfs(g, nb, curr, vis, rank, lowest_rank, critical)
          
            lowest_rank[curr] = min(lowest_rank[curr], lowest_rank[nb])
            
            if lowest_rank[nb] > rank[curr]:
                critical.append([curr, nb])

                    
    def create_graph(self, connections):
        g = defaultdict(list)
        for c in connections:
            g[c[0]].append(c[1])
            g[c[1]].append(c[0])       
        return g