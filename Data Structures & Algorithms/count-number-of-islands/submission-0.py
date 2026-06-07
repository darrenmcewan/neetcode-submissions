class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])
        def rec_island(r,c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return
            if grid[r][c] == "0":
                return
            else:
                grid[r][c] = "0"
                rec_island(r-1, c)
                rec_island(r+1, c)
                rec_island(r, c-1)
                rec_island(r, c+1)
        
        island_count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    island_count +=1
                    rec_island(r,c)
        return island_count

