# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        class TrieNode:
            def __init__(self):
                self.children = [None for _ in range(26)]
                self.end = False

        class Trie:
            def __init__(self):
                self.root = TrieNode()

            def add(self, word):
                curr = self.root
                for c in word:
                    val = ord(c) - ord('a')
                    if not curr.children[val]:
                        curr.children[val] = TrieNode()
                    curr = curr.children[val]
                curr.end = True

            def starts_with(self, word):
                curr = self.root
                wr = ''
                for c in word:
                    val = ord(c) - ord('a')
                    if not curr.children[val]:
                        return None
                    curr = curr.children[val]
                    wr += c
                    if curr.end:
                        return wr

                return None
        
        t = Trie()
        for word in dictionary:
            t.add(word)
        
        ans = []
        for word in sentence.split(' '):
            val = t.starts_with(word)
            if val != None:
                ans.append(val)
            else:
                ans.append(word)
            
        return ' '.join(ans)
        

        