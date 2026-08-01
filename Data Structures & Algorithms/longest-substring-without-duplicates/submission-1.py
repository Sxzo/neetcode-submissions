class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # expand r until theres a duplicate, at which popint you push left up until there is no longer that duplicate

        # zxyzxyz
        # 0123456

        l = 0 
        r = 0
        curr_substr = set()
        max_substr = 0
        while r < len(s):
            if s[r] not in curr_substr:
                curr_substr.add(s[r])
                max_substr = max(max_substr, len(curr_substr))
                r += 1
            else:
                while s[r] in curr_substr:
                    curr_substr.discard(s[l])
                    l += 1
        return max_substr


        