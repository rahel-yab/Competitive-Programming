class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        sett = set()
        ans = []
        i = 1
        while i <= len(words):
            ans.append(words[i-1])
            val = sorted(words[i-1])
            while i < len(words) and sorted(words[i]) == val:
                i += 1
            i+= 1
    
        return ans
            