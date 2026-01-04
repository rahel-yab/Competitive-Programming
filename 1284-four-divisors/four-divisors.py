class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:

        def factorization(n):
            factors = set()
            c = 1
            while c*c <= n:
                if n % c == 0:
                    factors.add(c)
                    factors.add(n//c)
                c += 1
            
            return factors
        
        ans = 0
        for num in nums:
            c = factorization(num)
            if len(c) == 4:
                ans += sum(list(c))
        return ans

