# Problem: Remove Max Number of Edges to Keep Graph Fully Traversable - https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size + 1)]
        self.rank = [0] * (size + 1)
        self.count = size

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx == rooty:
            return False
        if self.rank[rootx] > self.rank[rooty]:
            self.root[rooty] = rootx
        elif self.rank[rootx] < self.rank[rooty]:
            self.root[rootx] = rooty
        else:
            self.root[rooty] = rootx
            self.rank[rootx] += 1
        self.count -= 1
        return True

    def isConnected(self):
        return self.count == 1


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        dsua = UnionFind(n)
        dsub = UnionFind(n)
        c = 0

        for t, u, v in edges:
            if t == 3:
                flag = False
                if dsua.union(u, v):
                    flag = True
                if dsub.union(u, v):
                    flag = True
                if flag:
                    c += 1

        for t, u, v in edges:
            if t == 1:
                if dsua.union(u, v):
                    c += 1
            elif t == 2:
                if dsub.union(u, v):
                    c += 1

        if dsua.isConnected() and dsub.isConnected():
            return len(edges) - c
        return -1
