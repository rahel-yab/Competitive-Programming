class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def validate(mid):
            c = 0
            for num in nums:
                if num > mid:
                    c += ceil(num/mid) -1

            return c <= maxOperations

        low , high = 1 , max(nums)
        while low <= high:
            mid = (low+high) // 2
            if validate(mid):
                high = mid -1
            else:
                low = mid + 1
        
        return low