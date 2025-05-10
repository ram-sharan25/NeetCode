# The optmimum way to solve this is iwth dynamic programming 


#Recursive Approach
#Not accepted as this runs into infinite loop problem 
class Solution:
    def numDecodings(self, s: str) -> int:
        def dfs(i):
            if i==len(s):
                return 1
            if s[0] =='0':
                return 0
            res = dfs(i+1)
            if(i<len(s)-1):
                if(s[i]=='1' or s[i]=='2' and s[i+1]<'7'):
                    res+=dfs(i+2)
       
            return res
        return dfs(0)
                    
n = "12345"

eval = Solution()
out1 = eval.numDecodings(n)
print(out1)