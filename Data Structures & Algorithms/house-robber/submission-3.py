class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        robbed = [0] * n

        # base case (1 house, gotta rob it)
        robbed[0] = nums[0]
        if n > 1:
            robbed[1] = max(nums[0], nums[1])

            for i in range(2,n):
                robbed[i] = max(robbed[i-1], robbed[i-2]+nums[i])
                # which is more valuable, robbing the neighbor, or 
                # robbing two houses down + current
        return robbed[-1]
