from typing import List
print("Hello world")

n = 2

class Solution:
    #brute force
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def valid(s):
            open = 0
            for c in s :
                if c == "(" :
                    open += 1
                else:
                    open -=1
                if open<0: # if a single close appears before opening then invalid
                    return False
            return not open
        def generate_parenthesis(s:str):
            if n*2== len(s) :
                print("checking validity",s)
                is_valid = valid(s)
                if(is_valid):
                    res.append(s)
                return

            generate_parenthesis(s+"(")
            generate_parenthesis(s+")")

        generate_parenthesis("")
        print(res)
        return res

eval = Solution()
out1 = eval.generateParenthesis(n)
