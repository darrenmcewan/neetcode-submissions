class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Solution 1
        #return sorted(s) == sorted(t)
        
        # Solution 2
        #from collections import Counter
        #return Counter(s) == Counter(t)

        # Solution 3
        from collections import defaultdict

        if len(s) != len(t):
            return False
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        for i in range(len(s)):
            s_dict[s[i]]+=1
            t_dict[t[i]]+=1
        
        return s_dict == t_dict