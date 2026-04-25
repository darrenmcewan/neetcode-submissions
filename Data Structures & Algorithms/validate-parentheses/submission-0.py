class Solution:
    def isValid(self, s: str) -> bool:
        parens = {'(':')', '{':'}', '[':']'}
        stack = []

        for p in s:
            if p in parens:
                stack.append(p)
            else:
                if len(stack) == 0:
                    return False
                else: 
                    if parens[stack[-1]] != p:
                        return False
                    else:
                        stack.pop(-1)

        if len(stack) != 0:
            return False
        return True