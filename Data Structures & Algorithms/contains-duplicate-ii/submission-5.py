class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) <= 1:
            return False
        if k == 0:
            return False
        l,r = 0,1

        while r < len(nums):
            while abs(l-r)>k:
                l+=1
                r=l+1
            if nums[l] == nums[r]:
                return True
            r+=1
        return False