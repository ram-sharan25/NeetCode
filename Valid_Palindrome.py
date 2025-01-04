import re

s = "Was it a car or a  cat I saw?"
# s = "tab a cat"
# s = "0P0"


class Solution:
    # classic method
    def isPalindrome(self, s: str) -> bool:
        single_string =('').join(s.lower().split())
        pattern = r"[^a-z0-9]"
        only_characters = re.sub(pattern,"",single_string)
        total_characters = len(only_characters)
        mid_value =total_characters//2
        print(mid_value)
        print(len(only_characters))
        for i in range(mid_value):
            if(only_characters[i] != only_characters[(total_characters-1)-i]):
               return False
        print(single_string)
        print(only_characters)
        return True
    # reverse string method
    def isPalindrome_reverse_string(self, s: str) -> bool:
        single_string =('').join(s.lower().split())
        pattern = r"[^a-z0-9]"
        only_characters = re.sub(pattern,"",single_string)
        return only_characters[::]==only_characters[::-1]
    # Two Pointers
    def isPalindrome_two_pointers(self, s: str) -> bool:
        single_string =('').join(s.lower().split())
        pattern = r"[^a-z0-9]"
        only_characters = re.sub(pattern,"",single_string)
        l,r =0,len(only_characters)-1;
        while l<r:
            if only_characters[l]!= only_characters[r]:
                return False
            l +=1;
            r-=1;
        return True



eval = Solution()
out1 = eval.isPalindrome(s)
print("IS Pallindrome: ",out1)

out2 = eval.isPalindrome_reverse_string(s)
print("IS Pallindrome: ",out2)


out3 = eval.isPalindrome_two_pointers(s)
print("IS Pallindrome: ",out3)
