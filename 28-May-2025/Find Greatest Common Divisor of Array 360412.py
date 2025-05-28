# Problem: Find Greatest Common Divisor of Array - https://leetcode.com/problems/find-greatest-common-divisor-of-array/

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        # return math.gcd(max(nums), min(nums))
        mini = min(nums)
        maxi = max(nums)
        gcd = float('-inf')
        for i in range(1,mini+1):
            if mini % i == 0 and maxi % i == 0:
                gcd = max(gcd,i)
        return gcd