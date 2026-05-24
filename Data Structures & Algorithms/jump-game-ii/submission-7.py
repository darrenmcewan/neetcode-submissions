class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0,0 # set both pointers to the first position
        steps = 0
        while r < len(nums) - 1:
            furthest_idx = 0
            for i in range(l,r+1): #iterate through the pointers
                furthest_idx = max(furthest_idx, i + nums[i]) # find the furthest we can go between our two pointers
            l = r+1 # move the left pointer 1 past right
            r = furthest_idx #move right to the furthest
            steps += 1 # increment steps
        return steps