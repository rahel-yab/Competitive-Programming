class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left , right , either = 0 , 0 , 0
        for move in moves:
            if move == 'L':
                left += 1
            elif move == 'R':
                right += 1
            else:
                either += 1
        return max(left, right) + either - min(left , right)