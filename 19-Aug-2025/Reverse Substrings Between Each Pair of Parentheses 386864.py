# Problem: Reverse Substrings Between Each Pair of Parentheses - https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        ans = list(s)
        for i ,e in enumerate(s):
            if e == '(':
                stack.append(i+1)
            elif e == ')':
                ind = stack.pop()
                ans[ind:i] = reversed(ans[ind:i])
          
        val = []
        for i in ans:
            if i != '(' and i != ')':
                val.append(i)
        return ''.join(val)