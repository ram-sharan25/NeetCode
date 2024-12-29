#An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
import time



class Solution:
    def __init__(self):
       self.start_time = 0
       self.end_time = 0

    #Basic Solution
    def isAnagramBasic(self, s: str, t: str) -> bool:
        self.start_time = time.time()

        if(len(s)!=len(t)):
            self.end_time = time.time()
            return False
        s_set = set(s)
        t_set = set(t)
        if(s_set==t_set):
            combined = s+t
            for val in s_set:
                if ((combined.count(val)%2)==0):
                    self.end_time = time.time()
                    return True;
        self.end_time = time.time()
        return False

    #Using Sorted of Array
    def isAnagramSorted(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):return False
        else:
            return sorted(s)==sorted(t)

    #Using Hashtables
    def isAnagramHash(self,s:str,t:str) -> bool:
        if(len(s)!=len(t)):return False
        countS = {}
        countT = {}
        for i in range(len(s)):
            countS[s[i]] = 1+countS.get(s[i],0)
            countT[t[i]] = 1+countT.get(t[i],0)
        return countS==countT
    #using Hashtables second method
    def is_anagram_hash_2(self,s:str,t:str) -> bool:
        if(len(s)!=len(t)):return False
        countS = [0]*26
        countT = [0]*26
        for i,c in enumerate(s):
            countS[ord(s[i])-ord('a')] += 1
            countS[ord(c[i])-ord('a')] += 1
        return countS==countT


    def time_eval(self):
        return self.end_time-self.start_time


eval1 = Solution();
s = "baa"
t = "abaa"

out1 = eval1.isAnagramBasic(s,t)
print("AnagramBasicOutput ",out1)
print("Time taken",eval1.time_eval())
print()


eval2 = Solution()
out2 = eval2.isAnagramSorted(s,t)
print("SortedAnagramOutput ",out2)
print("Time Taken ",eval2.time_eval())


eval3 = Solution()
out3 = eval3.isAnagramHash(s,t)
print("HashAnagram ",out3)
print("Time Taken ",eval3.time_eval())

eval4 = Solution()
out4 = eval4.isAnagramHash(s,t)
print("HashAnagram ",out4)
print("Time Taken ",eval4.time_eval())
