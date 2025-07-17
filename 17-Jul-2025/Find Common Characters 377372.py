# Problem: Find Common Characters - https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        for i in range(ord('a') , ord('z') + 1):
            ch = chr(i)
            minn = float('inf')
            for word in words:
                minn = min(minn, word.count(ch))
                if minn == 0:
                    break
            res.extend([ch] * minn)
        return res

