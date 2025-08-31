# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        def factorial(num):
            if num == 0 or num ==1:
                return 1
            
            return num * factorial(num-1)
        
        val = factorial(n)
        c = 0
        while val:
            if val % 10 !=0:
                break
            else:
                c += 1
            val //= 10
        return c