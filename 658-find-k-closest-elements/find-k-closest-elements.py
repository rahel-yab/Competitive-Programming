class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ind = bisect_left(arr , x)
        left = ind -1
        right = ind
        ans = []

        while k:
            if left < 0:
                ans.append(arr[right])
                right += 1
            elif right >= len(arr):
                ans.append(arr[left])
                left -= 1
            
            elif abs(arr[left]- x) <= abs(arr[right] - x):
                ans.append(arr[left])
                left -= 1
            else:
                ans.append(arr[right])
                right += 1
            
            k-= 1
        
        return sorted(ans)


        