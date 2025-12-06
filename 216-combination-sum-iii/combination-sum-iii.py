class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        ans = []
        curr = []
        def backtrack(i , summ):
            if summ == n and len(curr) == k:
                ans.append(curr[:])
                return
            
            if summ > n or i > 9:
                return
            

            curr.append(i)
            backtrack(i+1 , summ+i)
            curr.pop()
            backtrack(i+1 , summ)
                
        backtrack(1 , 0)
        return ans
