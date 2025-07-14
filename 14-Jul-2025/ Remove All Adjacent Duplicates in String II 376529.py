# Problem:  Remove All Adjacent Duplicates in String II - https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  
        for ch in s:
            if stack and stack[-1][0] == ch:
                stack[-1] = (ch, stack[-1][1] + 1)
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append((ch, 1))
        ans = ''.join(ch * count for ch, count in stack)
        return ans
