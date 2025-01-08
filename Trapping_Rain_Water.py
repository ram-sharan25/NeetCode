from typing import List

height = [0,2,0,3,1,0,1,3,2,1]

class Solution:

    #my own solution
    def find_maximum(self,index:int)->list[int]:
        left_max_index,right_max_index = index,index
        right_array = height[index+1:]
        left_array  = height[0:index]

        if left_array:
             max_element_to_left = max(left_array);

             if max_element_to_left >= height[index]:
                 left_max_index = left_array.index(max_element_to_left)


        if right_array:
             max_element_to_right = max(right_array);
             if max_element_to_right >= height[index]:
                 right_max_index = (index+1)+right_array.index(max_element_to_right)
        return([left_max_index,right_max_index])


    def trap(self, height: List[int]) -> int:

        res=  0
        for i in range(len(height)):
            max_index = self.find_maximum(i)
            res += min(height[max_index[0]],height[max_index[1]])-height[i]
        return res

    # using array to store the left max and right max
    def trap_with_arrays(self, height: List[int]) -> int:
        res = 0 ;
        n = len(height);
        if n==0:
            return 0
        left_max = [0]*n;
        right_max = [0]*n;

        left_max[0] = height[0]
        for i in range(1,n):
            left_max[i] = max(max(height[0:i]),height[i])
        right_max[n-1] = height[n-1]
        for i in range(0,n-1):
            right_max[i] = max(max(height[i+1:]),height[i])
        for i in range(n):
            res += min(left_max[i],right_max[i])-height[i]
        return res

    # using stack
    #using two pointers
    def trap_with_two_pointers(self, height: List[int]) -> int:
        res = 0 ;
        l,r = 0,len(height)-1
        left_max,right_max = height[l],height[r]
        while l<r:
            if left_max<right_max:
                l+=1
                left_max = max(left_max,height[l])
                res += left_max-height[l]
            else:
                r-=1
                right_max = max(right_max,height[r])
                res += right_max-height[r]
        return res



eval  = Solution();
out1 = eval.trap(height)
print(out1)

out2 = eval.trap_with_arrays(height)
print(out2)
