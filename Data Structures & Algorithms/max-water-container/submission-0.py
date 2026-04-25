class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        max_area = 0
        while l < r:
            # Length * height`
            # Length = r - l
            # height = min(heights[r], heights[l])
            length = r-l
            height = min(heights[r], heights[l])
            max_area = max(max_area, length * height)
            if heights[r] > heights[l]:
                l+=1
            else:
                r-=1
        return max_area
