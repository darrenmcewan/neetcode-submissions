class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        max_area = 0
        # find the island start
        # sink land and increment counter
        # return counter as area 
        # compare against max_area

        def island_area(r,c, area):

            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return 0
            elif grid[r][c] == 0:
                return 0
            else:
                grid[r][c] = 0
                area =1 
                return area + island_area(r+1,c,area) + island_area(r-1,c,area) + island_area(r,c+1,area) + island_area(r,c-1,area)

                


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = island_area(r,c,0)
                    max_area = max(area,max_area)
                    

        return max_area

