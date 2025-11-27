class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)

        left = 0
        right = n
        ans = []
        i = 0
        while left <= right and i < n:
            if s[i] == 'I':
                ans.append(left)
                left += 1
            else:
                ans.append(right)
                right -= 1
            
            i+=1

        ans.append(left)
        return ans
            




