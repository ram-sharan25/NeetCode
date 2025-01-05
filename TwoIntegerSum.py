from typing import List

numbers = [2,3,4];
target = 6;
class Solution:
    # using set - Hashmap
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        store = set(numbers)
        for index,num in enumerate(numbers):
            reminaing_target = target-num;
            store.remove(num)
            if reminaing_target in store:
                return [index+1,numbers.index(reminaing_target)+1]
        return []
    # using binary search => as it is already sorted
    def twoSum_binary_search(self, numbers: List[int], target: int) -> List[int]:
        for index,num in enumerate(numbers):
            difference = target-num
            l ,r = index+1,len(numbers)-1
            while(l<=r):
                m = (l+r)//2
                if(numbers[m]==difference):
                    actual_index = numbers.index(difference)
                    small = min(index,actual_index)
                    large = max(index,actual_index)
                    return[small+1,large+1]
                elif numbers[m]>difference:
                    # m is already searched so , the end is m-1
                    r = m-1
                else:
                     # m is already searched so , the start is m+1
                    l = m+1

        return []
    # two pointers
    def twoSum_two_pointers(self, numbers: List[int], target: int) -> List[int]:
        for index,num in enumerate(numbers):
            difference = target-num
            l ,r = index+1,len(numbers)-1
            while(l<=r):
                if(numbers[l]==difference):
                    next_number = numbers.index(difference)
                    return[index+1,next_number +1]
                elif (numbers[r]==difference):
                    next_number = numbers.index(difference)
                    return[index+1,next_number +1]
                else:
                    l += 1
                    r -= 1

        return []


eval = Solution()
out1 = eval.twoSum(numbers,target)
print(out1)

out2 = eval.twoSum_binary_search(numbers,target)
print(out2)


out3 = eval.twoSum_two_pointers(numbers,target)
print(out3)
