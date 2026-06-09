class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1 and nums[0] < target:
            return 0

        l,r = 0,0
        minSizeArray = float('inf')
        curSum = 0
        for r in range(len(nums)):
            curSum += nums[r]
            while curSum >= target:
                minSizeArray = min(minSizeArray, r-l+1)
                
                curSum -= nums[l]
                l+=1


        if minSizeArray > len(nums):
            return 0
        else:
            return minSizeArray