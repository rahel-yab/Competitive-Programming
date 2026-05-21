class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        sett = set()
        for  num in arr1:
            pre = ''
            for ch in str(num):
                pre += ch
                sett.add(pre)
        
        ans = 0
        for num in arr2:
            pre = ''
            for ch in str(num):
                pre += ch
                if pre in sett:
                    ans = max(ans , len(pre))
        
        return ans 