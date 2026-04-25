class Solution:
    def isValid(self, s: str) -> bool:
        parens = {'(':')', '{':'}', '[':']'}
        stack = []

        for p in s:
            if p in parens:
                stack.append(p)
            elif not stack or parens[stack.pop()] != p:
                return False

        return not stack