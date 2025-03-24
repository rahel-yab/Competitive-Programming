# Problem: Construct Smallest Number From DI String - https://leetcode.com/problems/construct-smallest-number-from-di-string/description/

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        ans = []
        s = set()
        n = len(pattern)
        
        def backtrack(arr):
            if len(arr) == n + 1:
                ans.append("".join(arr))
                return 

            for i in map(str, range(1, 10)): 
                if i in s:
                    continue
                n2 = len(arr)
                if n2 == 0 or (
                    pattern[n2 - 1] == 'I' and arr[-1] < i) or (
                    pattern[n2 - 1] == 'D' and arr[-1] > i):

                    arr.append(i)
                    s.add(i)
                    backtrack(arr)
                    arr.pop()
                    s.remove(i)
        
        backtrack([])
        return ''.join(min(ans))