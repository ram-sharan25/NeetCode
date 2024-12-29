from collections import defaultdict
from typing import List
import operator
from heapq import nlargest


nums = [7,7,7,2,3,1,1,9,9,8,8,8,8]
k = 2

class Solution:
    #my solution
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        collection = defaultdict(int)
        final_values = []
        for val in nums:
            collection[val]+=1
        for i in range(k):
            max_val = max(collection.items(), key=operator.itemgetter(1))[0]
            del collection[max_val]
            final_values.append(max_val)
        print(final_values)
        return final_values

    # Heap Solution
    def top_k_frequent_heap(self, nums: List[int], k: int) -> List[int]:
        collection = defaultdict(int)
        final_values = []
        for val in nums:
            collection[val]+=1

        val = nlargest(k, collection.keys(), key=collection.get)
        print("val",val)
        return final_values



eval = Solution()
out = eval.topKFrequent(nums,2)
print(out)


eval = Solution()
out = eval.top_k_frequent_heap(nums,2)
print(out)
