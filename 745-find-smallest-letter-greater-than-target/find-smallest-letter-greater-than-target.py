class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low = 0
        high = len(letters) -1
        ans = -1
        while low <= high:
            mid = (low+high) //2
            if ord(letters[mid]) > ord(target):
                ans = letters[mid]
                high = mid -1             
            else:
                low = mid + 1
                
        return ans if ans != -1 else letters[0]