# Problem: Minimum Recolors to Get K Consecutive Black Blocks - https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution:  
    def minimumRecolors(self, blocks: str, k: int) -> int:  
        left = 0 
        minn = float('inf')
        ops = 0
        for right in range(len(blocks)):

            if blocks[right] == 'W':
                ops += 1

            if right - left + 1 == k:
                minn = min(minn, ops)
                if blocks[left] == 'W':
                    ops -= 1
                left += 1         
        
        return minn
