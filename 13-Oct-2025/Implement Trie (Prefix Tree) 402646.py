# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode():
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.end = False
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for i in word:
            val = ord(i) - ord('a')
            if not curr.children[val]:
                curr.children[val] = TrieNode()
            curr = curr.children[val]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for i in word:
            val = ord(i) - ord('a')
            if not curr.children[val]:
                return False
            curr = curr.children[val]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in prefix:
            val = ord(i) - ord('a')
            if  not curr.children[val]:
                return False
            curr = curr.children[val]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)