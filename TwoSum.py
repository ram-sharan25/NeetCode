from  typing import List
class Solution:
    #using brute force
    def two_sum_brute(self, nums: List[int], target: int) -> List[int]:
       for i in range(len(nums)):
           for j in range(i+1,len(nums)):
               if(nums[i]+nums[j] == target):
                   return [i,j]
       return []

    # using set and trivial solution
    def two_sum_set(self, nums: List[int], target: int) -> List[int]:
        first_index,second_index = 0,0;
        for i in range(len(nums)):
            diff =  target-nums[i];
            mutated_num = nums[i+1:len(nums)]
            mutated_set = set((mutated_num))

            if diff in mutated_set:
                first_index = i
                second_index = mutated_num.index(diff)+i+1
        return [first_index,second_index]

    # using sorting
    def two_sum_sorting(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i,num in enumerate(nums):
            A.append([num,i])
        A.sort();
        i,j = 0,len(nums)-1
        while i<j:
            current_sum = A[i][0]+A[j][0]
            if (current_sum == target):
                # the min max is to neutralize the effect of sorting in case
                # of negative numbers
                return [min(A[i][1],A[j][1]),max(A[i][1],A[j][1])]
            elif current_sum>target:
                j-=1
            else:
                i+=1
        return[]

    #using hashmaps
    def two_sum_hashmap_twopass(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i , n in enumerate(nums) :
            indices[n] = i;
        for i,n in enumerate(nums):
            diff =  target - n
            if (diff in indices) and (indices[diff]!=i):
                return [i,indices[diff]]
        return[]
    #using hasmaps one_pass
    def two_sum_hashmap_one_pass(self, nums: List[int], target: int) -> List[int]:
        prev_map = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev_map :
                return [prev_map[diff],i]
            prev_map[n] = i
        return[]

nums = [0,5,1,5]
target = 10;

eval = Solution()
out = eval.two_sum_set(nums,target)
print(out)

print()
out1 = eval.two_sum_brute(nums,target)
print(out1)

print()
out2 = eval.two_sum_sorting(nums,target)
print(out2)

print()
out2 = eval.two_sum_hashmap_twopass(nums,target)
print(out2)


print()
out3 = eval.two_sum_hashmap_one_pass(nums,target)
print(out3)
