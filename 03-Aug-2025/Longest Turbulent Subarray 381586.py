# Problem: Longest Turbulent Subarray - https://leetcode.com/problems/longest-turbulent-subarray/

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        if len(arr) == 2 and arr[0] != arr[1]:
            return 2
        if len(set(arr)) ==1:
            return 1
        maxx = 2
        left = 0
        right = 1
        while right < len(arr)-1:
            if arr[right-1] <= arr[right] <= arr[right+1] or  arr[right-1] >= arr[right] >= arr[right+1]:
                left = right
            else:
                maxx = max(maxx, right-left +2)
            right += 1
        return maxx

