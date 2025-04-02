# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = Counter(nums)
        def insertion_sort(bucket):
            for i in range(1, len(bucket)):
                key = bucket[i]
                j = i - 1
                while j >= 0 and bucket[j] > key:
                    bucket[j + 1] = bucket[j]
                    j -= 1
                bucket[j + 1] = key
                
            return bucket

        def bucket_sort(num_count, n):
            buckets = [[] for _ in range(n + 1)]
            for key , val in num_count.items():
                buckets[val].append(key)
            for bucket in buckets:
                insertion_sort(bucket)
            answer = []
            for bucket in buckets:
                answer.extend(bucket)
            res = []
            for i in range(len(answer) - 1, -1, -1):
                res.append(answer[i])
                if len(res) == k:
                    return res
            return res
        

        return bucket_sort(num_count, len(nums))