class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for ch in tokens:
            if ch=='+':
                op1=stack.pop()
                op2=stack.pop()
                stack.append(op2+op1)
            elif ch=='-':
                op1=stack.pop()
                op2=stack.pop()
                stack.append(op2-op1)
            elif ch=='*':
                op1=stack.pop()
                op2=stack.pop()
                stack.append(op2*op1)
            elif ch=='/':
                op1=stack.pop()
                op2=stack.pop()
                stack.append(int(float(op2)/op1))
            else:
                stack.append(int(ch))
        
        return stack[-1]
            