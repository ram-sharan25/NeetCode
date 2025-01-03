from typing import List

nums = [0,3,2,5,4,6,1,1]
# nums = [2,20,4,10,3,4,5]

# nums = [0,0]

class Solution:
    #brute force
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        res = 0
        for num in nums:
            current = num; streak = 0
            while current in store:
                current+=1
                streak+=1
            res = max(res,streak)
        return res
    # sorting
    def longestConsecutive_sorting(self, nums: List[int]) -> int:
        store = sorted(nums)
        res = 0
        streak = 1;
        if len(nums)<1:
            return 0
        if len(nums)==1:
            return 1
        for index in range(len(store)-1):
            current = store[index]; next_number = store[index+1]
            diff = next_number-current
            print(current,next_number,diff,streak)
            if diff==1:
                streak+=1
            elif diff==0:
                print("here",streak)
                res = max(res,streak)
                continue
            else :
                streak = 1
            res = max(res,streak)
            print(res)
        return res
    # hash set
    def longestConsecutive_hash_set(self, nums: List[int]) -> int:
        store = set(nums)
        res = 0
        for num in store:
            if(num-1) not in  store:
                streak = 1
                while (num+streak) in store:
                    streak+=1
                res = max(res,streak)
        return res
    # hash map
    def longestConsecutive_hash_map(self, nums: List[int]) -> int:
        store = set(nums)
        res = 0
        for num in store:
            if(num-1) not in  store:
                streak = 1
                while (num+streak) in store:
                    streak+=1
                res = max(res,streak)
        return res





eval  = Solution();
out1 = eval.longestConsecutive(nums)
print("Longest Subsequence :",out1)

out2 = eval.longestConsecutive_sorting(nums)
print("Longest Subsequence Sorted :",out2)

out3 = eval.longestConsecutive_hash_set(nums)
print("Longest Subsequence Hasmap :",out3)
