from typing import List
from collections import defaultdict

strs = ["act","pots","tops","cat","stop","hat"]

class Solution:
    #my_solution
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        collection = {}
        for each_string in strs:
            sorted_string = ''.join(sorted(each_string))
            if sorted_string in collection:
                collection[sorted_string].append(each_string)
            else:
                collection[sorted_string] = [each_string]

        final_values = list(collection.values())        # print(final_values)
        return final_values

    # using defaultdict
    def group_anagrams_default_dict(self, strs: List[str]) -> List[List[str]]:
        collection = defaultdict(list)
        for each_string in strs:
            sorted_string = ''.join(sorted(each_string))
            collection[sorted_string].append(each_string)
        final_values = list(collection.values())
        return final_values
    #hashmap second method
    def group_anagrams_default_dict_2(self, strs: List[str]) -> List[List[str]]:
        collection = defaultdict(list)
        for each_string in strs:
            chars = [0]*26
            for s in each_string:
                chars[ord(s)-ord('a')] +=1
            collection[tuple(chars)].append(each_string)
        final_values = list(collection.values())
        return final_values




eval = Solution()
out = eval.group_anagrams(strs)
print("Grouped Anagram List",out)

print()
out = eval.group_anagrams_default_dict(strs)
print("Grouped Anagram List default dict",out)

print()
out = eval.group_anagrams_default_dict_2(strs)
print("Grouped Anagram List default dict 2",out)
