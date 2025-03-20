# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        child = [0] * k
        min_unfairness= float("inf")
        def backtrack(i):
            nonlocal min_unfairness
            if i >= len(cookies):
                min_unfairness = min(min_unfairness,max(child))

                return
            for j in range(k):
                child[j] += cookies[i]
                backtrack(i+1)
                child[j] -= cookies[i]
                if child[j] == 0:
                    break

            return min_unfairness
        return backtrack(0)