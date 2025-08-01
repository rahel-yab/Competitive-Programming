# Problem: Check if array is sorted - https://practice.geeksforgeeks.org/problems/check-if-an-array-is-sorted0701/1

class Solution:
    def isSorted(self, arr) -> bool:
        # code here
        left = 0
        right = 1
        while right < len(arr):
            if arr[right] < arr[left]:
                return False
            right += 1
            left += 1
        return True