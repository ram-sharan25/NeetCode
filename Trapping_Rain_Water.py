from typing import List
print("Hello World")

height = [0,2,0,3,1,0,1,3,2,1]

class Solution:
    def find_maximum(self,index:int)->list[int]:
        left_max_index,right_max_index = index,index
        right_array = height[index+1:]
        left_array  = height[0:index]

        print("right array",right_array)
        print("left array",left_array)

        if left_array:
             max_element_to_left = max(left_array);
             print("left element",max_element_to_left)
             if max_element_to_left >= height[index]:
                 left_max_index = left_array.index(max_element_to_left)
                 print("left index",left_max_index)

        if right_array:
             max_element_to_right = max(right_array);
             print("right element",max_element_to_right)
             if max_element_to_right >= height[index]:
                 right_max_index = (index+1)+right_array.index(max_element_to_right)
                 print("right index",right_max_index)
        return([left_max_index,right_max_index])


    def trap(self, height: List[int]) -> int:
        print(height)
        res=  0
        for i in range(len(height)):
            max_index = self.find_maximum(i)
            print()
            print("main index",max_index)
            print()
            res += min(height[max_index[0]],height[max_index[1]])-height[i]
        print("Res",res)
        return res

eval  = Solution();
out1 = eval.trap(height)
print(out1)
