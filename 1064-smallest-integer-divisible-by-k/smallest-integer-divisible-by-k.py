class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0:
            return -1
        
        sett = set()

        i , l = 1 , 1

        while i % k:
            if i in sett:
                return -1
            sett.add(i)
            i = 10*(i%k) + 1
            l += 1

        
        return l