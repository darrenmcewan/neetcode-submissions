class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0] #guaranteed len(nums) > 0
        maxEnding = nums[0] #Current subarray sum

        for i in range(1,len(nums)): # starting at index 
            maxEnding = max(maxEnding + nums[i], nums[i])
            res = max(res, maxEnding)
        
        return res