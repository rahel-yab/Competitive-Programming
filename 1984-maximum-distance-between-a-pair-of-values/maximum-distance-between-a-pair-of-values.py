class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        # ans = 0

        # def binary_search(target):
        #     low = 0
        #     high = len(nums2)-1

        #     while low <= high:
        #         mid = (low+high) // 2
        #         if nums2[mid] >= target:
        #             low = mid + 1
        #         else:
        #             high = mid -1

        #     return high

        # for i , num in enumerate(nums1):
        #     ind = binary_search( num)
        #     ans = max(ans , ind-i)

        # return ans 


        left , right = 0 , 1
        while left < len(nums1) and right < len(nums2):
            if nums1[left] > nums2[right]:
                left += 1
            right += 1
        return max(0 , right - left -1)