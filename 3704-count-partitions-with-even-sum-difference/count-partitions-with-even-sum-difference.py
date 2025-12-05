class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]

        for i in range(1 , n):
            prefix[i] = prefix[i-1] + nums[i]

        ans = 0
        for i in range(n-1):
            left = prefix[i]
            right = prefix[-1] - left
            if (left-right) % 2 == 0:
                ans += 1
        return ans
