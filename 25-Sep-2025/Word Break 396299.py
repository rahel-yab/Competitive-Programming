# Problem: Word Break - https://leetcode.com/problems/word-break/description/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        sett = set(wordDict)
        memo = {}

        def dp(i):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]

            for word in sett:
                if s.startswith(word, i):
                    if dp(i + len(word)):
                        memo[i] = True
                        return True

            memo[i] = False
            return False

        return dp(0)