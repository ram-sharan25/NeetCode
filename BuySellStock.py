from typing import List


#prices = [10,1,5,6,7,1]
#prices = [10,8,7,5,2]
#prices=[5,1,5,6,7,1,10]
prices=[2,1,2,1,0,1,2]

class Solution:
    # brute force
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)-1):
            max_val = max(prices[i+1:])
            diff = max_val - prices[i]
            if diff > res:
                res = diff

        return res
    #two pointer solution
    def maxProfit_two_pointer(self, prices: List[int]) -> int:
        l,r= 0,1
        res = 0
        while (l<r and r<len(prices)):
            left = prices[l]
            right = prices[r]
            diff = right-left
            if diff > res:
                res = diff
            if left>right:
               l = r
            r+=1

        return res
    # dynamic prograaming
    def maxProfit_dynamic(self, prices:List[int])->int:
        res = 0
        minBuy = prices[0]

        for sell in prices:
            res = max(res,sell-minBuy)
            minBuy = min(minBuy,sell)
        return res

eval = Solution()
out1 = eval.maxProfit(prices)
print(out1)

out2 = eval.maxProfit_two_pointer(prices)
print(out2)

out3 = eval.maxProfit_dynamic(prices)
print(out3)
