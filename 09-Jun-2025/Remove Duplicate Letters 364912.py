# Problem: Remove Duplicate Letters - https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {char: idx for idx, char in enumerate(s)} 
        stack = []
        seen = set()
        
        for i, char in enumerate(s):
            if char in seen:
                continue           
            while stack and stack[-1] > char and last[stack[-1]] > i:
                seen.remove(stack.pop())             
            stack.append(char)
            seen.add(char)
        
        return ''.join(stack)
