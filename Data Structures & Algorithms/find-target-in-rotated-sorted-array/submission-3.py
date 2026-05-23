class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums) - 1

        # Goal: find inflection point - then run binary search on both halves to find the target

        while l < r:
            mid = (l+r) // 2 

            if nums[mid] > nums[r]: # inflection point is to the right
                l = mid + 1
            elif nums[mid] < nums[r]: # inflection point is to the left
                r = mid
        inflection = l

        l,r = 0,inflection - 1
        while l <= r:
            mid = (l+r) // 2 
            if nums[mid] < target:
                l=mid+1
            elif nums[mid] > target:
                r = mid-1
            else:
                return mid
        
        l,r = inflection, len(nums) - 1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid-1
            else:
                return mid
        return -1



 # Input [3,4,5,6,1,2]
 # Inflection = ^