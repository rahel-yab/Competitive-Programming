# Problem: K Closest Points to Origin - https://leetcode.com/problems/k-closest-points-to-origin/

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        res = []
        for i in range(len(points)):
            u , v = points[i]
            dist = u**2 + v**2
            heapq.heappush(ans,[dist,i])
        
        for i in range(k):
            ind = heapq.heappop(ans)[1]
            res.append(points[ind])
        return res