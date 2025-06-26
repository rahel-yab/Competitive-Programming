# Problem: Freedom Trail - https://leetcode.com/problems/freedom-trail/

class Solution:
    def findRotateSteps(self, ring: str, key: str):
        n = len(ring)
        mapp = defaultdict(list)
        for i, val in enumerate(ring):
            mapp[val].append(i)

        q = deque()
        q.append((0, 0))
        visited = [{} for _ in range(len(key)+1)]
        visited[0][0] = 0

        for i in range(len(key)):
            curr = mapp[key[i]]
            nextt = defaultdict(lambda: float('inf'))
            while q:
                pos, steps = q.popleft()
                for np in curr:
                    dist = abs(pos - np)
                    move = min(dist, n - dist)
                    ans = steps + move + 1
                    if ans < visited[i+1].get(np, float('inf')):
                        visited[i+1][np] = ans
                        q.append((np, ans))
            q = deque([(pos, val) for pos, val in visited[i+1].items()])
        return min(visited[len(key)].values())