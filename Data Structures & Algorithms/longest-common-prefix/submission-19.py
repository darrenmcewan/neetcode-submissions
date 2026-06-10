class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        found = False
        max_len = len(strs[0])
        if not strs:
            return ""
        if len(strs[0]) == 1:
            return strs[0]

        # Check 
        for i,letter in enumerate(strs[0]):
            if strs[-1][i] != letter:
                max_len = i
                break
            else:
                found = True
            
                

        if found == False: 
            return ''
        elif max_len == len(strs[0]):
            return strs[0]
        else:
            return strs[0][:i]