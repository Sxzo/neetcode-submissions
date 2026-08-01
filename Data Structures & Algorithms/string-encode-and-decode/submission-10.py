class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}#{s}"
        
        return res


    def decode(self, s: str) -> List[str]:
        print(s)
        i = 0 
        res = []
        while i < len(s):
            tmp = ""
            while s[i] != '#':
                tmp += s[i]
                i += 1
            i += 1
            print(tmp)
            str_len = int(tmp)

            individual_str = ""
            for j in range(str_len):
                individual_str += s[i]
                i += 1
            
            res.append(individual_str)
        
        return res

            




