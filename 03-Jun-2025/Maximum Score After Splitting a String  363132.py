# Problem: Maximum Score After Splitting a String  - https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution:
    def maxScore(self, s: str) -> int:
        maxx = float('-inf')
        s = list(int(i) for i in s)
        for i in range(1,len(s)):
            right = s[i:]
            left = s[:i]
            rsum = sum(right)
            if left == 0:
                lsum = 1
            else:
                lsum = sum(left)
            maxx = max(maxx, rsum + len(left)- lsum)
        return maxx

