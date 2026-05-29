class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = float("inf")
        for num in nums:
            curr_sum = sum(int(i) for i in str(num))
            ans = min(ans , curr_sum)
        
        return ans
