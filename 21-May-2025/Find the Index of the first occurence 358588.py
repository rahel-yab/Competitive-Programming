# Problem: Find the Index of the first occurence - https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left = 0
        while left <= len(haystack) - len(needle):
            c = 0
            for right in range(len(needle)):
                if haystack[left+right] != needle[right]:
                    break
                else:
                    c += 1
            if c == len(needle):
                return left
            left += 1
        return -1