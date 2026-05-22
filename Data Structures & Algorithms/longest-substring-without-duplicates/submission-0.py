class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlength = 0
        l,r = 0,0
        substr = set()
        for r in range(len(s)):

            while s[r] in substr:
                substr.remove(s[l])
                l+=1
            substr.add(s[r])
            maxlength = max(maxlength, r-l+1)
                
        return maxlength
