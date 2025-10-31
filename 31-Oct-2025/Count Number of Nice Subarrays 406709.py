# Problem: Count Number of Nice Subarrays - https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        even_odd = [0] * n
        for i , num in enumerate(nums):
            if num & 1:
                even_odd[i] = 1
        prefix = 0
        dictt = defaultdict(int)
        dictt[0] = 1
        ans = 0
        for num in even_odd:
            prefix += num
            if prefix - k in dictt:
                ans += dictt[prefix-k]
            dictt[prefix] += 1
        return ans
        