class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
        
        # sort dict based on value
        sorted_hash = {k:v for k,v in sorted(hashmap.items(), key=lambda item: item[1], reverse=True)}
        limit_hash = list(sorted_hash.keys())
        return limit_hash[:k]