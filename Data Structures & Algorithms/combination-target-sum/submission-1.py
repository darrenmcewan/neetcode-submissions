class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        currSet = []
        total = 0
        def recSum(i, currSet, total):

            if total == target:
                output.append(currSet.copy())
                return
            if i >= len(nums) or total > target:
                return 

            
            currSet.append(nums[i])
            recSum(i, currSet, total + nums[i])

            currSet.pop()
            recSum(i+1, currSet, total)


        recSum(0,currSet, total)
        return output
