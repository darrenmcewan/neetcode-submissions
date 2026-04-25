class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}
        for i, num in enumerate(nums):
            if target - num in hashset:
                return sorted([i, hashset[target-num]])
            else:
                hashset[num] = i
        
