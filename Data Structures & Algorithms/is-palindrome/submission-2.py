class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for char in s:
            if char.isalnum():
                new_s += char.lower()
        
        s = new_s
        left = 0
        right = len(s) - 1

        while left < right:
            while not s[left].isalnum():
                left += 1
            
            while not s[right].isalnum():
                right -= 1

            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True


        