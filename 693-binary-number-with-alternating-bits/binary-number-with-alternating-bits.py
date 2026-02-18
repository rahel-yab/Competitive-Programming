class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = None
        while n:
            if n & 1:
                if prev == 1:
                    return False       
                prev = 1
            else:
                if prev == 0:
                    return False 
                prev = 0
            n >>= 1
        
        return True