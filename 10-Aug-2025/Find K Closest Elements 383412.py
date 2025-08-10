# Problem: Find K Closest Elements - https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        ind = bisect_left(arr, x)
        res = deque()
        if ind == 0:
            return arr[:k]
        if ind == n:
            return arr[-k:]

        left = ind - 1
        right = ind

        while k > 0:
            if left < 0:
                res.append(arr[right])
                right += 1
            elif right >= n:
                res.appendleft(arr[left])
                left -= 1
            elif abs(arr[left] - x) <= abs(arr[right] - x):
                res.appendleft(arr[left])
                left -= 1
            else:
                res.append(arr[right])
                right += 1
            k -= 1

        return list(res)