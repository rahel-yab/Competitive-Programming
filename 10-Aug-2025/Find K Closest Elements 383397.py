# Problem: Find K Closest Elements - https://leetcode.com/problems/find-k-closest-elements/

from bisect import bisect_left
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ind = bisect_left(arr, x)
        left = ind - 1
        right = ind
        res = []

        while k > 0:
            if left < 0:
                res.append(arr[right])
                right += 1
            elif right >= len(arr):
                res.append(arr[left])
                left -= 1
            elif abs(arr[left] - x) <= abs(arr[right] - x):
                res.append(arr[left])
                left -= 1
            else:
                res.append(arr[right])
                right += 1
            k -= 1

        return sorted(res)