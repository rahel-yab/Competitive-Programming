# Problem: Clear Digits - https://leetcode.com/problems/clear-digits/description/

class Solution:
    def clearDigits(self, s: str) -> str:
        ans = []
        for i in s:
            if i.isdigit():
                if ans:
                    ans.pop()
            else:
                ans.append(i)
        return ''.join(ans)