from typing import List
import re
print("Hello World")

tokens = ["1","2","+","3","*","4","-"]
tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        store =[]
        for exp in tokens:
            print(store)
            if exp=="+":
                val1 = store.pop()
                val2 = store.pop()
                val = (val1)+(val2)
                store.append(val)
            elif exp=="*":
                val1 = store.pop()
                val2 = store.pop()
                val = (val1)*(val2)
                store.append(val)
            elif exp=="-":
                val1 = store.pop()
                val2 = store.pop()
                val = (val2)-(val1)
                store.append(val)
            elif exp=="/":
                val1 = store.pop()
                val2 = store.pop()
                val = int(float(val2)/val1)
                store.append(val)
            else:
                store.append(int(exp))

        return store[0]



evaluate = Solution()
out1 = evaluate.evalRPN(tokens)
print(out1)
