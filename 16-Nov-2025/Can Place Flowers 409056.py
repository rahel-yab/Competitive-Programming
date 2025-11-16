# Problem: Can Place Flowers - https://leetcode.com/problems/can-place-flowers/

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n== 1 and flowerbed[0] == 0 and len(flowerbed) == 1:
            return True
        if n== 0 and flowerbed[0] == 0 and len(flowerbed) == 1:
            return True

        ans = 0

        for i in range(len(flowerbed)):
            if i == 0:
                if flowerbed[i] == 0 and flowerbed[1] == 0:
                    flowerbed[0] = 1
                    ans += 1

            if i!= 0 and i !=len(flowerbed) -1 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0:
                ans += 1
                flowerbed[i] = 1

            if i == len(flowerbed) -1:
                if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                    flowerbed[i] = 1
                    ans += 1
    
        return ans >= n

            