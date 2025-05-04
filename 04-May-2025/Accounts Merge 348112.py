# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class UnionFind:
    def __init__(self,size):
        self.root = [i for i in range(size)]
        self.rank = [0] * size

    def find(self,x):
        while self.root[x] != x:
            self.root[x] = self.root[self.root[x]]
            x = self.root[x]
        return self.root[x]
    
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
 

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = UnionFind(len(accounts))
        mapp = {}
        for i,acc in enumerate(accounts):
            for email in acc[1:]:
                if email in mapp:
                    dsu.union(i, mapp[email])
                else:
                    mapp[email] = i
        
        dictt = defaultdict(list)
        for e,i in mapp.items():
            leader = dsu.find(i)
            dictt[leader].append(e)

        res = []
        for i,emails in dictt.items():
            name = accounts[i][0]
            res.append([name] + sorted(emails))

        return res
        
        