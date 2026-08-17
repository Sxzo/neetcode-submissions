class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []

        def bt(index, curr_str, curr_res):
            if index >= len(s):
                if len(curr_str) == 0:
                    res.append(curr_res[:])
                return
            
            print(index, curr_str, curr_res)
            
            curr_str += s[index]
            
            if len(curr_str) > 0 and curr_str[::-1] == curr_str:
                curr_res.append(curr_str)
                bt(index + 1, "", curr_res[:])
                curr_res.pop()
                bt(index + 1, curr_str, curr_res[:])
            else:
                bt(index + 1, curr_str, curr_res[:])


        bt(0, "", [])
        return res
        