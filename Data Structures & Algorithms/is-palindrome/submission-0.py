class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for char in s:
            if char.isalnum():
                new_s += char.lower()
        s = new_s

        units_counted = 0 
        left = 0
        right = len(s) - 1

        while left < right:
            if len(s) % 2 != 0 and units_counted == len(s) - 1: 
                return True 
            
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
            units_counted += 2
        
        return True


        