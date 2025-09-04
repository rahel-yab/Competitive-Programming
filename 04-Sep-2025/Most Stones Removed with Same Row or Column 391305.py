# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if self.rank[rootx] < self.rank[rooty]:
            self.root[rootx] = rooty
        elif self.rank[rootx] > self.rank[rooty]:
            self.root[rooty] = rootx
        else:
            self.root[rooty] = rootx
            self.rank[rootx] += 1
    
    def connected(self,x,y):
        return self.find(x) == self.find(y)
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        dsu = UnionFind(n)
        for i in range(n):
            x1 , y1 = stones[i]
            for j in range(i+1, n):
                x2 , y2 = stones[j]
                if x1 == x2 or y1 == y2:
                    dsu.union(i,j)
        
        val = len(set(dsu.find(i) for i in range(n)))
        return n - val