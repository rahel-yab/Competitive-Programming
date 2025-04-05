# Problem: Number of Pairs Satisfying Inequality - https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        count = 0
        n = len(nums1)
        new = [0] * n
        for i in range(n):
            new[i] = nums1[i] - nums2[i]
        def merge(left_half,right_half) -> List[int]:
            nonlocal count
            left, right = 0, 0
            merged = []
            while left < len(left_half) and right < len(right_half):
                if left_half[left] <= right_half[right]:
                    merged.append(left_half[left])
                    left += 1
                else:
                    merged.append(right_half[right])
                    right += 1
            
            while left < len(left_half):
                merged.append(left_half[left])
                left += 1
                
            while right < len(right_half):
                merged.append(right_half[right])
                right += 1
            
            l , r = 0,0
            while l < len(left_half) and r < len(right_half):
                if left_half[l] <= right_half[r] + diff:
                    count += len(right_half) - r
                    l += 1
                else:
                    r += 1
            
            return merged
        def mergeSort(left, right, arr):
            if left == right:
                return [arr[left]]
            mid = (left + right)//2
            left_half = mergeSort(left, mid, arr)
            right_half = mergeSort(mid+1, right,arr)
            return merge(left_half, right_half)
        mergeSort(0, n - 1, new)
        return count