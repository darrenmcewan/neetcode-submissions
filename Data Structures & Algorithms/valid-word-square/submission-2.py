class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        num_rows = len(words)

        for r in range(num_rows):
            row_word = words[r]
            col_word = ""
            for c in range(num_rows):
                if r < len(words[c]):
                    col_word += words[c][r]
            
            if row_word != col_word:
                return False
        
        return True
