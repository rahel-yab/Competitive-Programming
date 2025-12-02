class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        
        def count(n):
            c = 0
            while n:
                if n&1:
                    c += 1
                n >>= 1
            
            return c
        
        ans = 0
        for num in range(left , right+1):
            curr = count(num)
            if curr in [2 , 3, 5 , 7 , 11 , 13 , 17 , 19]:
                ans += 1
        
        return ans