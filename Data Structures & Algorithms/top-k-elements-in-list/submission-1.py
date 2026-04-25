class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1

        import heapq
        result = heapq.nlargest(k, hashmap.keys(), key=hashmap.get)
        return result