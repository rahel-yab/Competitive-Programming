class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        row , col = len(mat) , len(mat[0])
    
        prefix = mat 
        for r in range(row):
            for c in range(1 , col):
                prefix[r][c] = mat[r][c] + prefix[r][c-1]

        def get_sum(r1, c1, r2, c2):
            return prefix[r2][c2] - prefix[r1][c2] - prefix[r2][c1] + prefix[r1][c1]

        def valid(side):
            for r in range(row - side + 1):
                for c in range(col - side + 1):
                    summ = 0
                    for i in range(r, r + side):
                        row_sum = prefix[i][c + side - 1]
                        if c > 0:
                            row_sum -= prefix[i][c - 1]
                        summ += row_sum
                    if summ <= threshold:
                        return True
            return False

        low ,  high = 1 , min(row , col)
        ans = 0
        while low <= high:
            mid = (low+high) // 2
            if valid(mid):
                ans = mid
                low = mid + 1        
            else:
                high = mid -1
        
        return ans 