class Solution:
    def trap(self, height: List[int]) -> int:
        # Look for the first peak
        # move until you find a new peak
        water_trapped = 0

        peak_map = {}

        for i in range(len(height)):
            peak_map[i] = (max(height[:i], default=0), max(height[i:], default=0))
            water_trapped += max(min(peak_map[i][0],peak_map[i][1]) - height[i],0)

        return water_trapped
        
        