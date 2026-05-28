class Solution:
    def longestPalindrome(self, s: str) -> str:
        # initialize longest palindrome
        longest_palindrome = s[0]

        for i in range(len(s)):
            ## Even
            l,r = i,i+1
            while l >= 0 and r < len(s) and s[l]==s[r]:
                l-=1
                r+=1
            
            longest_palindrome = max(longest_palindrome, s[l+1:r], key=len)
            ## Odd
            l,r = i,i
            while l>=0 and r < len(s) and s[l]==s[r]:
                l-=1
                r+=1

            longest_palindrome = max(longest_palindrome, s[l+1:r], key=len)
        
        return longest_palindrome

        
