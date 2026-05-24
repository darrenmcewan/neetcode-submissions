class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0,0 # set both pointers to the first position
        steps = 0
        while r < len(nums) - 1:
            furthest_idx = 0
            for i in range(l,r+1): #iterate through the pointers
                furthest_idx = max(furthest_idx, i + nums[i])
            l = r+1
            r = furthest_idx
            steps += 1
        return steps