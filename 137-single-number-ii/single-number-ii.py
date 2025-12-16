class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        
        for i in range(32):
            count = 0
            for num in nums:
                if num & (1<<i):
                    count += 1

            rem = count % 3
            if rem:
                ans |= 1 << i
                
        if ans >= (1 << 31):
            ans -= (1 << 32)
        
        return ans


