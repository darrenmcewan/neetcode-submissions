class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if s and not t:
            return False
        
        j=0
        curr = s[j]

        for i,letter in enumerate(t):
            if letter == curr:
                j+=1
                if j == len(s):
                    return True
                curr = s[j]
            else:
                continue
        return False


                    
