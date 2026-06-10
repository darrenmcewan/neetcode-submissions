class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0,len(heights)-1

        maxWater = 0

        while l < r:
            waterArea = min(heights[r], heights[l]) * (r-l)
            maxWater = max(waterArea, maxWater)

            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1

        return maxWater