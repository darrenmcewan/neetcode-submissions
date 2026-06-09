class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        seen = set()

        l,r=0,0
        max_substr = 0

        for r in range(len(s)):
            if s[r] in seen:
                while s[r] in seen:
                    seen.discard(s[l])
                    l+=1


            
            seen.add(s[r])
            
            max_substr = max(max_substr, r-l+1)


        return max_substr