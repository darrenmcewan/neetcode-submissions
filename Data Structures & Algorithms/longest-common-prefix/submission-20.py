class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs.sort()
        max_len = min([len(x) for x in strs])
        i = 0
        for i in range(max_len):
            if strs[0][i] != strs[-1][i]:
                return strs[0][:i]
        return strs[0]