from collections import defaultdict
from typing import List
import operator
from heapq import nlargest


nums = [7,7,7,2,3,1,1,9,9,8,8,8,8,14,8,8,8,8,8,8,8,8,8]
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
        return final_values

    # Heap Solution
    def top_k_frequent_heap(self, nums: List[int], k: int) -> List[int]:
        collection = defaultdict(int)
        for val in nums:
            collection[val]+=1
        final_values = nlargest(k, collection.keys(), key=collection.get)
        return final_values

    #Bucket Sort
    def top_k_frequent_bucket(self, nums: List[int], k: int) -> List[int]:
        collection = defaultdict(int)
        freq = [[] for i in range(len(nums)-1) ]
        for val in nums:
            collection[val]+=1
        for val,cnt in collection.items():
            freq[cnt].append(val)
        final_output = []
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                final_output.append(num)
                if len(final_output)==k:
                    return final_output
        return []





eval = Solution()
out = eval.topKFrequent(nums,2)
print(out)



out1 = eval.top_k_frequent_heap(nums,2)
print(out1)


out2 = eval.top_k_frequent_bucket(nums,2)
print(out2)
