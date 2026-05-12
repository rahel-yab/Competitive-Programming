class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key= lambda x : x[1]-x[0], reverse=True)
        curr = tasks[0][1] - tasks[0][0]
        start , add = tasks[0][1] , 0
        for u , v in tasks[1:]:
            if curr < v:
                add += v - curr
                curr = v
            curr -= u
        
        return start + add
                