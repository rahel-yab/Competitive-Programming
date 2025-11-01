# Problem: Count ways to group overlapping ranges - https://leetcode.com/problems/count-ways-to-group-overlapping-ranges/

class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        def binary_exponentiation(base , exp):
            ans = 1
            while exp:
                if exp & 1:
                    ans *= base % MOD
                base *= base % MOD
                exp >>= 1
            return ans

        ranges.sort()
        ans = []
        ans.append(ranges[0])
        for i in range(1 , len(ranges)):
            u , v = ans[-1]
            x , y = ranges[i]
            if x <= v:
                ans[-1] = [u , max(y, v)]
            else:
                ans.append([x , y])

        res = binary_exponentiation(2 , len(ans))
        return res % MOD
