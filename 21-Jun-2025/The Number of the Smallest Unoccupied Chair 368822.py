# Problem: The Number of the Smallest Unoccupied Chair - https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/description/

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        arrivals = [(times[i][0], i) for i in range(n)]
        arrivals.sort()
        chairs = list(range(n))
        heapq.heapify(chairs)
        leaving = []
        for t, ind in arrivals:
            while leaving and leaving[0][0] <= t:
                heapq.heappush(chairs, heapq.heappop(leaving)[1])
        
            chair = heapq.heappop(chairs)
            if ind == targetFriend:
                return chair
            heapq.heappush(leaving, (times[ind][1], chair))
        
        return -1

        