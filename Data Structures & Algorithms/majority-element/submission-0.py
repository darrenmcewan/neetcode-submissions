class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        hashmap = defaultdict(int)

        for num in nums:
            hashmap[num] += 1

        for key in hashmap:
            if hashmap[key] >= n / 2:
                return key
                