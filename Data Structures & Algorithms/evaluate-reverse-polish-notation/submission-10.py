class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c in ["*", "-", "+", "/"]:
                a = int(stack.pop())
                b = int(stack.pop())
                if c == "*":
                    stack.append(a*b)
                elif c == "+":
                    stack.append(a+b)
                elif c == "-":
                    stack.append(b-a)
                elif c == "/":
                    stack.append(int(b/a))
                print(stack)
            else:
                stack.append(c)
        
        return int(stack[0])
        
        # (((1 + 2) * 3) * 4)
            
