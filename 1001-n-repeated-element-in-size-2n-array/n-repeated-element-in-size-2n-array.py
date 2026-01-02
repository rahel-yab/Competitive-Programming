class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) //2
        count = Counter(nums)
        for key , val in count.items():
            if val == n:
                return key