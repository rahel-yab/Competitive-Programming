# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class UnionFind:
    def __init__(self,size):
        self.root = [i for i in range(size)]
        self.rank = [0] * size
    
    def find(self,x):
        while self.root[x] != x:
            self.root[x] = self.root[self.root[x]]
            x = self.root[x]
        return x
    
    def union(self,x,y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.root[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.root[rootx] = rooty
            else:
                self.root[rooty] = rootx
                self.rank[rootx] += 1
    def is_connected(self,x,y):
        return self.find(x) == self.find(y)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dsu = UnionFind(n)
        heap = []
        for i in range(n):
            x1,y1 = points[i]
            for j in range(i+1,n):
                x2,y2 = points[j]
                weight = abs(x2-x1) + abs(y2-y1)
                heappush(heap,(weight,i,j))
        ans = 0
        count = 0
        while heap:
            weight, x , y = heappop(heap)
            if dsu.is_connected(x,y) == False:
                dsu.union(x,y)
                ans += weight
                count += 1
            # else:
            #     dsu.union(x,y)
            if count == n-1:
                return ans
        return ans


            