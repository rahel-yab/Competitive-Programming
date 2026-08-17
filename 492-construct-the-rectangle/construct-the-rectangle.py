class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        w = 1
        for i in range(1, int(sqrt(area)) + 1):
            if area%i == 0:
                w = i
        return [area//w , w]
