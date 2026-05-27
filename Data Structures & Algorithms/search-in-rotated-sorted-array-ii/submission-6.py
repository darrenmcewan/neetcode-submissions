class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l,r = 0, len(nums)-1
        while l <= r:
            middle = (l+r) // 2
            if nums[middle] == target:
                return True
            if nums[l] < nums[middle]:
                if nums[l] <= target < nums[middle]:
                    r = middle - 1
                else: 
                    l = middle + 1
            
            elif nums[l] > nums[middle]:
                if nums[middle] < target <= nums[r]:
                    l = middle + 1
                else:
                    r = middle - 1
            elif nums[l] == nums[middle]:
                l+=1
            else:
                l+=1

                

        
        return False
