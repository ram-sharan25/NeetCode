from typing import List
# height = [1,7,2,5,4,7,3,6]
height = [2,2,2]

''' required solution in O(1) space complexity
and  O(n) time complexity
If I  use brute force then space complexity will be O(1) but
  time complexity will be O(n^2)
If I use hashmap, set, then both time and space complexity
will be O(n).
The viable solution to use for this is two pointer. '''
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0,len(heights)-1
        res = 0
        while l<r:
            area = min(heights[l],heights[r])*(r-l)
            res =  max(res,area)
            if(heights[l]<=heights[r]):
                l+=1
            else:
                r-=1
        return res






eval  = Solution();
out1 = eval.maxArea(height)
print(out1)
