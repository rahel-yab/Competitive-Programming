class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s):
            s = list(s)
            for i , bit in enumerate(s):
                s[i] = str(int(bit) ^ 1)
            
            return ''.join(s)

        
        def find(n):
            if n == 1:
                return '0'
            
            val = find(n-1)
            return val + '1' + invert(val)[::-1]
        
        s = find(n)
        return s[k-1]