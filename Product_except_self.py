from collections import defaultdict
from  typing import List

nums = [1,2,4,6]


class Solution:
    # O(n^2)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        collection = defaultdict(int)
        for i in range(len(nums)):
            product = 1
            for j,val in enumerate(nums):
              if(i!=j):
                  product *=val
            collection[i] = product
        return list(collection.values())
    #O(n)
    def product(self, nums:List[int]) -> List[int]:
        prod,zero_cnt = 1,0
        for num in nums:
            if num:
                prod *=num
            else:
                zero_cnt+=1

        # if more than one zeros then all the numbers are zero
        if zero_cnt>1: return [0]*len(nums)

        res = [0]*len(nums)
        for i,num in enumerate(nums):
            #no zero condition
            if zero_cnt  == 0:
                res[i] = prod//num
            else:
                res[i] = prod if  num==0 else 0 # zero for all except zero number index
        return res

    # O(n) with suffix and prefix'
    def product_prefix_suffix(self,nums:List[int])->List[int]:
        n = len(nums)
        prefix = [0] * n;
        suffix = [0] * n;
        prod = [0] * n;
        prefix[0] = suffix[n-1] = 1
        for i in range(1,n):
            prefix[i]=  nums[i-1]*prefix[i-1]
        for i in range(n-2,-1,-1):
            suffix[i]=  nums[i+1]*suffix[i+1]
        print(suffix,prefix)
        for i in range(n):
            prod[i] = prefix[i]*suffix[i]
        print(prod)
        return prod

      # O(n) with suffix and prefix optimal solution
    def product_prefix_suffix_optimal(self,nums:List[int])->List[int]:
        n = len(nums)
        prod = [1] * n;
        prefix =  1

        for i in range(0,n):
            prod[i] = prefix
            prefix*=nums[i]
        postfix= 1
        for i in range(n-1,-1,-1):
            prod[i] *=postfix
            postfix *=nums[i]
        return prod



eval = Solution()
out1 = eval.productExceptSelf(nums)
print(out1)

out2  = eval.product([1,2,3])
print(out2)

out3  = eval.product_prefix_suffix([1,2,3,0])
print(out3)

out4  = eval.product_prefix_suffix_optimal([5,2,3,4,5])
print(out4)
