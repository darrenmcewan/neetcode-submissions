class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        i = 0
        for j in range(1,len(nums)):
            if nums[i]%2 == nums[j]%2:
                return False
            i+=1
        return True
                