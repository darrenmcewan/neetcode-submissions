class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l,r = 0,k

        while r <= len(nums):
            res.append(max([nums[x] for x in range(l,r)]))
            l+=1
            r+=1
        return res