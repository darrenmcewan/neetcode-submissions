class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        ROWS,COLS = len(board), len(board[0])
        letter_idx = 0

        def dfs(r,c,letter_idx, word):

            if letter_idx == len(word):
                return True        
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != word[letter_idx]:
                return False

            if letter_idx == len(word) - 1:
                return True


            temp = board[r][c]
            board[r][c] = "#"
            for dr, dc in directions:
                if dfs(r + dr, c + dc, letter_idx + 1, word):
                    return True
            board[r][c] = temp
            return False



        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    # Check neighbors
                    if dfs(r,c,letter_idx, word):
                        return True


                    

        return False