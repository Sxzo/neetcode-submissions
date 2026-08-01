class Solution:

    def encode(self, strs: List[str]) -> str:
        # Decode with a integer representing the length of the string 

        encoded_string = ""

        for string in strs:
            encoded_string += (str(len(string)) + "-" + string)
        print(encoded_string)
        return encoded_string
            

    def decode(self, s: str) -> List[str]:
        decoded_list = []

        index = 0
        
        while index < len(s):
            length = ""
            while s[index] != "-":
                length += s[index]
                index += 1
            
            index += 1 # Start at the first character
            
            length = int(length)

            remaining_characters = length - 1
            temp_string = ""
            
            while remaining_characters >= 0:
                temp_string += s[index]
                index += 1
                remaining_characters -= 1
            
            decoded_list.append(temp_string)

        return decoded_list

            