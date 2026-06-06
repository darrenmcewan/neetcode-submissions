class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        order = {"I": 0, "V": 1, "X": 2, "L": 3, "C": 4, "D": 5, "M": 6}

        res = 0

        if len(s) == 1:
            return mapping[s]
        
        else:
            for i in range(len(s)-1):
                if order[s[i]] < order[s[i+1]]:
                    res-=mapping[s[i]]
                else:
                    res+=mapping[s[i]]
            res+=mapping[s[-1]]
                
        

        return res

                
            