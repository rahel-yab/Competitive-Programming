class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        right_1 = []
        for row in grid:
            last = -1
            for ind , j in enumerate(row):
                if j == 1:
                    last = ind
            right_1.append(last)

        swaps = 0
        for i in range(n):
            limit = i 
            idx = -1
            for j in range(i, n):
                if right_1[j] <= limit:
                    idx = j
                    break
        
            if idx == -1:
                return -1
        
            while idx > i:
                right_1[idx], right_1[idx - 1] = right_1[idx - 1], right_1[idx]
                swaps += 1
                idx -= 1
                
        return swaps