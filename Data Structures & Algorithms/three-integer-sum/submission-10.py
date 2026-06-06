class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #nums = [1,2,3]
        output = set()

        for i in range(len(nums)): # i = 0
            l,r = i+1, len(nums)-1 # l = 1, r = 2
            
            target = -nums[i] #target = -1
            
            while l < r:
                if nums[l]+nums[r] == target:
                    threeSum = [nums[i], nums[l], nums[r]]
                    threeSum.sort()
                    output.add(tuple(threeSum))
                    l+=1
                    r-=1
                elif nums[l] + nums[r] < target:
                    l+=1
                elif nums[l] + nums[r] > target: 
                    r-=1
            



        return list(output)


