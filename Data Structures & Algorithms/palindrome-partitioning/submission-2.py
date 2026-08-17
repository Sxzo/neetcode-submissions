class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []
        path = []
        def bt(index, curr_str):
            if index >= len(s):
                if len(curr_str) == 0:
                    res.append(path[:])
                return
            
            curr_str += s[index]
            
            if len(curr_str) > 0 and curr_str[::-1] == curr_str:
                path.append(curr_str)
                bt(index + 1, "")
                path.pop()
            bt(index + 1, curr_str)


        bt(0, "")
        return res
        