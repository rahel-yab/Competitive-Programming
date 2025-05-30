# Problem: Ugly Number - https://leetcode.com/problems/ugly-number/description/

class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        prime = set()
        while n % 2 == 0:
            n //= 2
            prime.add(2)
        for i in range(3, int(n ** 0.5) + 1, 2):
            while n % i == 0:
                prime.add(i)
                n //= i
        if n > 2:
            prime.add(n)
        for i in prime:
            if i != 2 and i != 5 and i != 3:
                return False
        return True