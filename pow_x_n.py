class Solution:
    # brute force
    def myPow(self, x: float, n: int) -> float:
        res = 1
        for i in range(abs(n)):
            if(n>0):
                res*=x
            else :
                res/=x
        return res
    # binary exponentation
    def myPow_exp(self,x:float,n:int) ->int:
        def helper(x,n):
            print(x,n)
            if x==0:
                return 0
            if n==0:
                return 1
            res = helper(x*x,n//2)
            print("finally evaluated",res,x,n)
            return res*x if n%2 else res
        res = helper(x,abs(n))
        print("IN the final",res)
        return res if (n>=0) else 1/res

x= 3 ; n = 6;

eval = Solution ()
out1 = eval.myPow_exp(x,n)
