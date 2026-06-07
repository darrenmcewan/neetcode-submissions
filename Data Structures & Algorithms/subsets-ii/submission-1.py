class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = [] 
        currSets = []
        nums.sort()


        def rec(i):
            if i >= len(nums):
                subsets.append(currSets.copy())
                return
            
            # opt 1 include i
            currSets.append(nums[i])
            rec(i+1)

            currSets.pop()
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i += 1
            
            rec(i+1)

            # opt 2 exclude i






        rec(0)
        return subsets