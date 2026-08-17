class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []

        def bt(i, curr_str):
            if i == len(digits):
                res.append(curr_str)
                return
            
            for char in digitToChar.get(digits[i]):
                bt(i + 1, curr_str + char)
        
        bt(0, "")

        return res

        