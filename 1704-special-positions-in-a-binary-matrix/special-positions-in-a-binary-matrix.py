class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        r  , c = len(mat),  len(mat[0])
        row_sum = []
        for row in mat:
            row_sum.append(sum(row))
        col_sum = []
        for col in zip(*mat):
            col_sum.append(sum(col))


        ans = 0
        for i in range(r):
            for j in range(c):
                if row_sum[i] == 1 and col_sum[j] == 1 and mat[i][j] == 1:
                    ans += 1
        
        return ans

        
