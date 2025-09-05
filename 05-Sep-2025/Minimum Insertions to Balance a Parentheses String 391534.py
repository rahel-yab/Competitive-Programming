# Problem: Minimum Insertions to Balance a Parentheses String - https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/

class Solution:
    def minInsertions(self, s: str) -> int:
        stack = []
        ans = 0
        i = 0
        n = len(s)

        while i < n:
            if s[i] == '(':
                stack.append(i)

            elif stack and s[stack[-1]] == '(' and s[i] == ')' and i + 1 < n and s[i + 1] == ')':
                stack.pop()
                i += 1 

            elif stack and s[stack[-1]] == '(' and s[i] == ')' and (i + 1 >= n or s[i + 1] != ')'):
                ans += 1 
                stack.pop()

            elif not stack and s[i] == ')' and i + 1 < n and s[i + 1] != ')':
                ans += 2  
            elif not stack and s[i] == ')' and i + 1 < n and s[i + 1] == ')':
                ans += 1 
                i += 1  

            elif not stack and s[i] == ')' and i + 1 >= n:
                ans += 2  

            i += 1

        ans += 2 * len(stack)  
        return ans