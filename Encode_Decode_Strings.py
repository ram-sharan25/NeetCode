from typing import List


#  input = ["neet","code","love","you"]
input = ["","hello","","deep"]

class Solution:
    #mysolution
    def encode(self, strs: List[str]) -> str:
        strs = ['-2' if val == "" else val for val in strs]
        concat_string =  '-1'.join(strs)
        val_encoded = [ord(char)+index for index,char in enumerate(concat_string)]
        encoded_string = ''.join([chr(val) for val in val_encoded])
        return encoded_string

    def decode(self, s: str) -> List[str]:
        if len(s)<=0:return []
        each_char = [chr(ord(c)-i) for i,c in enumerate(s)]
        combined_str = ''.join(each_char)
        decoded_string = combined_str.split("-1")
        res = ["" if s=="-2" else s for s in decoded_string ]
        return res

    #optimalsolution from suggestion
    def encode1(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res+=str(len(s))+"#"+s
        return res

    def decode1(self,s:str):
        res = []
        i = 0
        while i < len(s):
            j = i ;
            while (s[j]!= "#"):
                j+=1
            length = int(s[i:j])
            i = j+1
            j = i+length
            res.append(s[i:j])
            i=j
        return res

print()
eval = Solution()
encoded_string = eval.encode(input)
print(encoded_string)
decoded_string = eval.decode(encoded_string)
print(decoded_string)

print()
encoded_string1 = eval.encode1(input)
print(encoded_string1)
decoded_string1 = eval.decode1(encoded_string1)
print(decoded_string1)
