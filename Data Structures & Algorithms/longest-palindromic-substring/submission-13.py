class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen_Palindrome = s[0]

        for i in range(len(s)):

            # even palindromes
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l-=1
                r+=1
            
            maxLen_Palindrome = max(maxLen_Palindrome, s[l+1:r], key=len)

            l,r = i,i
            while l>= 0 and r<len(s) and s[l] == s[r]:
                l-=1
                r+=1
            
            maxLen_Palindrome = max(maxLen_Palindrome, s[l+1:r], key=len)

        return maxLen_Palindrome