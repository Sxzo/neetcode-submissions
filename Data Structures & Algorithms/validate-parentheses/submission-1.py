class Solution:
    def isValid(self, s: str) -> bool:

        # Queue = FIFO
        # Stack = LIFO 
        # stack = []

        stack = []

        for c in s:
            if c == "{" or c == "[" or c == "(":
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                
                pop_val = stack.pop()
                
                if (c == "}" and pop_val == "{") or (c == "]" and pop_val == "[") or (c ==")" and pop_val == "("):
                    continue
                else:
                    return False


        return len(stack) == 0
        