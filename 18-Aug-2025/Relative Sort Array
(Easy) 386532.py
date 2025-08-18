# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        ans = []
        sorted_arr1 = sorted(arr1)
        for i in arr2:
            for _ in range(count[i]):
                ans.append(i)
        for i in sorted_arr1:
            if i not in arr2:
                ans.append(i)
        return ans
        
