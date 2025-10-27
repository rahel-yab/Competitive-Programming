# Problem: Removing Minimum Number of Magic Beans - https://leetcode.com/problems/removing-minimum-number-of-magic-beans/

class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        ans = float("inf")
        total = sum(beans)
        for i in range(len(beans)):
            val = total-(beans[i]*(len(beans)-i))
            ans = min(ans , val)
        return ans
            
                

