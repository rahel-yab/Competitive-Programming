# Problem: Count Number of Distinct Integers After Reverse Operations - https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        sett = set(nums)
        for num in nums:
            # print(str(num)[::-1])
            val = int(str(num)[::-1])
            if val not in sett:
                sett.add(val)
        return len(sett)