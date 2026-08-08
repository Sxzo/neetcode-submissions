class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # For each window, keep track of a mapping of char: frequency 
        # The moment that it becomes impossible to create a valid string, move left up

        left = 0
        right = 0

        curr_map = defaultdict(int)
        max_len = 0
        maxf = 0
        while right < len(s):
            curr_map[s[right]] += 1
            maxf = max(maxf, curr_map[s[right]])

            while (right - left + 1 - maxf) > k:
                curr_map[s[left]] -= 1
                left += 1
                maxf = max(curr_map.values())
            
            max_len = max(max_len, (right - left + 1))
            right += 1
        
        return max_len



        