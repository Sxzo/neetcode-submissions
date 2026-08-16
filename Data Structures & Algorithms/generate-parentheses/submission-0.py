class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def bt(paren_str, o, c):
            if o == 0 and c == 0:
                res.append(paren_str)
                return
            
            if o == 0: 
                paren_str += ")"
                bt(paren_str, o, c - 1)
            elif o == c:
                paren_str += "("
                bt(paren_str, o - 1, c)
            else:
                paren_str += "("
                bt(paren_str, o - 1, c)
                paren_str = paren_str[0:len(paren_str)- 1]
                paren_str += ")"
                bt(paren_str, o, c - 1)
        
        bt("", n, n)
        return res