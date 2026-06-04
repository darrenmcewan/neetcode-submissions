class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        need = t[i]

        for j in range(len(s)):
            if s[j] == need:
                i+=1
                if i == len(t):
                    return 0
                need = t[i]
        
        return len(t[i:])

                
