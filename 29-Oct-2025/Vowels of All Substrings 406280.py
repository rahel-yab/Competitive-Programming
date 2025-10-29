# Problem: Vowels of All Substrings - https://leetcode.com/problems/vowels-of-all-substrings/

class Solution:
    def countVowels(self, word: str) -> int:
        vowles = set(['a' , 'e' , 'i' , 'o' , 'u'])
        n = len(word)
        count = 0
        for i , c in enumerate(word):
            if c in vowles:
                count += (i+1) * (n-i)

        return count