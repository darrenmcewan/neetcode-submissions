class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        required_letter_counts = {}
        for letter in t:
            if letter in required_letter_counts:
                required_letter_counts[letter] += 1
            else:
                required_letter_counts[letter] = 1
        
        window = defaultdict(int)
        have = 0
        need = len(required_letter_counts)

        res = [-1,-1]
        resLen = float('infinity')

        l,r = 0,0

        while r < len(s):
            window[s[r]] += 1
            if s[r] in required_letter_counts and window[s[r]] == required_letter_counts[s[r]]:
                have+=1
            
            while have == need:
                if (r-l+1) < resLen:

                    res = [l,r+1]
                    resLen = r-l+1

                
                window[s[l]] -= 1
                if s[l] in required_letter_counts and window[s[l]] < required_letter_counts[s[l]]:
                    have -= 1
                l+=1

            r+=1
        return s[res[0]:res[1]]