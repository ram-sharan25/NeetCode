from typing import List
# This program is to check for the duplication of numbers in
# the list of numbers

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setVal = set((nums))
        if(len(setVal)<len(nums)): return True
        return False


nums = [1,2,3]
eval =Solution()
print(eval.hasDuplicate(nums))
