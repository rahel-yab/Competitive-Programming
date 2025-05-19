# Problem: Bitwise XOR of All Pairings - https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=problem-list-v2&envId=brainteaser

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        xor = 0
        for num in nums2:
            xor ^= num

        print(xor)
        if m % 2 == 0:
            if n % 2 == 0:
                return 0
            else:
                return xor
        else:
            if n % 2 == 0:
                curr = 0
                for num in nums1:
                    curr ^= num
                return curr
            else:
                for num in nums1:
                    xor ^= num
                return xor

        
        

        