# Problem: People are leaving - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/A

class UnionFind:
    def __init__(self,size):
        self.root = [i for i in range(size + 2)]
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
            self.root[rootx] = rooty
    def is_connected(self,x,y):
        return self.find(x) == self.find(y)

n, m = map(int,input().split())
dsu = UnionFind(n+1)
for _ in range(m):
    y, x = map(str,input().split())
    x = int(x)
    if y == '?':
        val = dsu.find(x)
        if val > n:
            print(-1)
        else:
            print(val)
    else:
        dsu.union(x,x +1)