class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)-1 , -1 , -1):
            num = nums[i]
            while num:
                n = num % 10
                ans.append(n)
                num //= 10
        return list(reversed(ans))