# Problem: 2 Keys Keyboard - https://leetcode.com/problems/2-keys-keyboard/description/

class Solution:
    def minSteps(self, n: int) -> int:
        def factorization(k):
            factors = defaultdict(int)
            d = 2
            while d*d <= k:
                while k % d == 0:
                    factors[d] += 1
                    k //= d
                d += 1
            if k >= 2:
                factors[k] = 1
            return factors
        
        primes = factorization(n)
        ans = 0
        for key , val in primes.items():
            ans += key * val
        return ans