class Solution:
    def checkDivisibility(self, n: int) -> bool:
        summ , prod , num = 0 , 1 , n
        while n:
            r = n % 10
            summ += r
            prod *= r  
            n //= 10
        
        return num % (summ+prod) == 0