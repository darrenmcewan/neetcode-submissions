class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        res = 0
        for x in tokens:
            if x == "+":
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op1 + op2)
            elif x == "-":
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op1 - op2)              
            elif x == "*":
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op1 * op2)
            elif x == "/":
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(int(op1 / op2))

            else:
                stack.append(int(x))
            
        return stack[0]