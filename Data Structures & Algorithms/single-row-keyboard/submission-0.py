class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        letter_pos = {}

        for i, letter in enumerate(keyboard):
            letter_pos[letter] = i
        
        curr = 0
        total_time = 0
        for letter in word:
            total_time += abs(curr - letter_pos[letter])
            curr = letter_pos[letter]
        
        return total_time