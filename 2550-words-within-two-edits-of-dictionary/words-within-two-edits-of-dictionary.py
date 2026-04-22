class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []
        for word in queries:
            for word2 in dictionary:
                cnt , flag = 0  , False
                for i in range(len(word)):
                    if word[i] != word2[i]:
                        cnt += 1
                if cnt <= 2:
                    ans.append(word)
                    flag = True
                if flag:
                    break
        return ans
