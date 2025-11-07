# Problem: Number of Laser Beams in a Bank - https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        secure = []
        for i in bank:
            val = i.count('1')
            if val != 0:
                secure.append(val)
        
        ans = 0
        for i in range(1 , len(secure)):
            ans += secure[i] * secure[i-1]

        return ans
        

