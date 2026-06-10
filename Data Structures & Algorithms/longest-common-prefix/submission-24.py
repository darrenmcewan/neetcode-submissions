class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs.sort()
        max_len = len(strs[0])
    
        for i in range(max_len):
            if strs[0][i] != strs[-1][i]:
                return strs[0][:i]
        return strs[0]