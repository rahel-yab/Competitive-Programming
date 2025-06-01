# Problem: Count Vowel Substrings of a String - https://leetcode.com/problems/count-vowel-substrings-of-a-string/description/

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        count = 0 
        curr = set() 
        for i in range(len(word)):
            if word[i] in 'aeiou':
                curr.add(word[i])       
                for j in range(i+1, len(word)): 
                    if word[j] in 'aeiou':
                        curr.add(word[j])
                    else:
                        break        
                    if len(curr) == 5:
                        count += 1					
            curr = set()
                        
        return count