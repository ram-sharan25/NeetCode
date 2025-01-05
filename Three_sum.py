from typing import List

nums = [-1,0,1,2,-1,-4]

class Solution:
    def twoIntegerSum(self,nums: List[int],val:int)->List[List]:
        res = []
        for index, num in enumerate(nums):
            l,r = index+1,len(nums)-1
            difference = 0-val-num
            print("interation",val,num,difference)
            while (l<=r):
                if(nums[l]==difference):
                    res.append([num,difference])
                    l+=1
                elif(nums[r]==difference):
                    res.append( [num,difference])
                    r-=1
                else:
                    l+=1
                    r-=1
        return res
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        for index,num  in enumerate(nums):
            two_sum_array  = nums[index+1:]
            print("Original Array",num,two_sum_array)
            two_sum = self.twoIntegerSum(two_sum_array,num)
            print("found array",num,two_sum)
            if (len(two_sum)>0):
                for x in two_sum:
                    triple_sum  = [num,*x]
                    if(sorted(triple_sum) not in res):
                        res.append(sorted([num,*x]))
        return res

eval = Solution()
out1 = eval.threeSum(nums)
print(out1)
