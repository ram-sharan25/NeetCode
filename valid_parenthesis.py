s = "(()])"
#s="()[]{}"
#s="([{}])"
class Solution:

    #my solution
    def check_validity (self,a:str,b:str):
        if a=="{" and b =="}":
            return True
        elif a=="[" and b =="]":
            return True
        elif a=="(" and b==")":
            return True
        else :return False

    def isValid(self, s: str) -> bool:
        store = []
        count = 0
        for i in range(0,len(s)):
            if(len(store)):
                current_val = store.pop()
                if self.check_validity(current_val,s[i]):
                    count+=1
                    continue
                else:
                    store.append(current_val)
            store.append(s[i])
        return count==len(s)//2
    # elegant solution
    def isValid_object(self, s: str) -> bool:
        store = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        for i in range(0,len(s)):
            print(store)
            if(len(store)):
                current_val = s[i]
                if current_val in closeToOpen:
                    #print(store[-1],closeToOpen[current_val])
                    if closeToOpen[current_val] == store[-1]:
                        store.pop()
                        continue
            store.append(s[i])
        return True if not store else False


eval = Solution()
out1 = eval.isValid(s)
print(out1)

out1 = eval.isValid_object(s)
print(out1)
