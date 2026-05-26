class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        processed = []
        cnt = 0
        for ch in word:
            if ch.upper() in word and ch.lower() in word and ch not in processed:
                cnt += 1
                processed.append(ch.lower())
                processed.append(ch.upper())
        return cnt