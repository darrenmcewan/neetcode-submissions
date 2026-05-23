class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        maxSum = -1
        nums.sort()

        l,r = 0,len(nums) - 1

        while l < r:
            sum = nums[l] + nums[r]
            if sum < k:
                l+=1
                maxSum = max(maxSum, sum)
            elif sum >= k:
                r-=1

        return maxSum
        


