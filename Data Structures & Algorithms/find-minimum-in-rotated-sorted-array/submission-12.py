class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        

        while l < r:
            if nums[l] <= nums[r]:
                return nums[l]
            middle = (l+r) // 2

                     
            if nums[middle] > nums[r]:
                l = middle + 1
            elif nums[middle] < nums[r]:
                r = middle
        return nums[l]

        


            
            
                