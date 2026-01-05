class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        ans = 0
        c = 0
        minn , summ  = float("inf") , 0 
        for row in matrix:
            for num in row:
                ans += abs(num)
                if num < 0:
                    c += 1
                minn = min(minn , abs(num))
    
        if c% 2==1:
            ans -=(2*minn)
        
        return ans

