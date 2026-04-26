class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        return max(
            self.rob_linear(nums[:-1]),  # exclude last
            self.rob_linear(nums[1:])    # exclude first
        )
    
    def rob_linear(self,nums):
        prev2, prev1 = 0, 0
        for num in nums:
            prev2, prev1 = prev1, max(prev1, prev2 + num)
        return prev1
        

