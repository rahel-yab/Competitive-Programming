class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        cnt = 0
        for string in patterns:
            if string in word:
                cnt += 1
        return cnt