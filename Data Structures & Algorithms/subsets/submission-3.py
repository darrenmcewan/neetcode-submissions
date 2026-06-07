class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        currSet = []

        def recSubsets(subsets, currSet, nums, i):

            if i >= len(nums):
                subsets.append(currSet.copy())
                return
            
            currSet.append(nums[i])
            recSubsets(subsets, currSet, nums, i+1)
            
            currSet.pop()
            recSubsets(subsets, currSet, nums, i+1)
            
            
            
            
            





        
        recSubsets(subsets, currSet, nums, 0)
        return subsets