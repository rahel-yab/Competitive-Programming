class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapp = {'2':'abc' , '3':'def' , '4':'ghi' , '5':"jkl" , '6':"mno" , '7':'pqrs' , '8':'tuv' , '9':"wxyz"}

        ans = []
        def backtrack(i , curr):
            if i == len(digits):
                ans.append(curr)
                return
                
            for ch in mapp[digits[i]]:
                backtrack(i+1 , curr + ch)
        backtrack(0 , "")
        return ans
        
        
        

