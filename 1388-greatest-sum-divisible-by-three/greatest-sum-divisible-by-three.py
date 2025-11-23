class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        summ = sum(nums)
        val = summ % 3
        
        if val == 0:
            return summ

        rem1 = []
        rem2 = []
        
        for num in nums:
            remainder = num % 3
            if remainder == 1:
                rem1.append(num)
            elif remainder == 2:
                rem2.append(num)

        rem1.sort()
        rem2.sort()
        rem1 = rem1[:2]
        rem2 = rem2[:2]
        
        min_removal = float('inf')

        if val == 1:
            if len(rem1) >= 1:
                min_removal = min(min_removal, rem1[0])
            
            if len(rem2) >= 2:
                min_removal = min(min_removal, rem2[0] + rem2[1])

        elif val == 2:
            if len(rem2) >= 1:
                min_removal = min(min_removal, rem2[0])
                
            if len(rem1) >= 2:
                min_removal = min(min_removal, rem1[0] + rem1[1])

        if min_removal == float('inf'):
            return 0
        else:
            return summ - min_removal

