class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        output = 0
        
        def palindrome(l,r):
            res = 0
            
            while s[l] == s[r]:
                if l < 0 or r > len(s)-1:
                    return res
                res += 1
                l-=1
                r+=1
                if l < 0 or r > len(s)-1:
                    return res
            return res
        
        for i in range(len(s)):
            output += palindrome(i,i)
        for i in range(len(s)-1):
            output += palindrome(i,i+1)
        
        return output
        



        

            

                