# Problem: Sum of Prefix Scores of Strings - https://leetcode.com/problems/sum-of-prefix-scores-of-strings/description/

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        class TrieNode():   
            def __init__(self):
                self.children = [None for _ in range(26)]
                self.end = False
                self.count =0
            
        class Trie():
            def __init__(self):
                self.root = TrieNode()
            def add(self, word):
                curr = self.root
                for c in word:
                    ind = ord(c) - ord('a')
                    if not curr.children[ind]:
                        curr.children[ind] = TrieNode()         
                    curr = curr.children[ind]
                    curr.count += 1
                curr.end = True
            
            def prefix(self, word):
                curr = self.root
                for c in word:
                    ind = ord(c) - ord('a')
                    if not curr.children[ind]:
                        return 0
                    curr = curr.children[ind]
                return curr.count
        
        t = Trie()
        for word in words:
            t.add(word)
        
        ans = []
        for word in words:
            curr = t.root
            res = 0
            for i in word:
                ind = ord(i) - ord('a')
                curr = curr.children[ind]
                res += curr.count
            ans.append(res)
        return ans