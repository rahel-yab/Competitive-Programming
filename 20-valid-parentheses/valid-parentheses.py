class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        stack = []
        stack.append('*')
        for i in range(n):
            if s[i] in ['(', '{', '[']:
                stack.append(s[i])
            elif s[i] == ')' and stack[-1]=='(':
                stack.pop()
            elif s[i] == ']' and stack[-1]=='[':
                stack.pop()
            elif s[i] == '}' and stack[-1]=='{':
                stack.pop()
            else:
                stack.append('+')

        if stack[-1] == '*':
            return True
        return False

