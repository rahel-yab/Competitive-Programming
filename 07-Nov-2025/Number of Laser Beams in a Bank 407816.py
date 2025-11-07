# Problem: Number of Laser Beams in a Bank - https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        secure = []
        for i in bank:
            val = sum(1 if j == '1' else 0 for j in i)
            if val != 0:
                secure.append(val)
        
        left = 0
        right = 1
        ans = 0
        while right < len(secure):
            ans += secure[left] * secure[right]
            left += 1
            right += 1
        return ans
        

