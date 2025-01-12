s1="abc"
s2="bbbca"

class Solution:
    # my solution
    def checkInclusion(self, s1: str, s2: str) -> bool:
        res = True
        for c in s1:
            if c not in s2:
                res = res and False
            else:
                s2 = s2.replace(c,"",1)



        return res
    # my solution
    def checkInclusion_window(self, s1: str, s2: str) -> bool:
        for index,c in enumerate(s2):
            if c  in s1:
                res = True
                i = 0
                new_String = s2[index:index+len(s1)]
                while i <(len(s1)):
                    if s1[i] not in  new_String:
                        res = res and False
                    else:
                        new_String =  new_String.replace(s1[i],"",1)
                    i+=1
                if res:
                    return res

        return False
    #my solution  optimal
    # this has time complexity of O(n*m^2)
    def checkInclusion_window_optimal(self, s1: str, s2: str) -> bool:
        r = 0
        # this contributes to O(n)
        while r < len(s2):
            if s2[r] in s1:
                res = True
                l = 0
                # this is O(m)
                new_String = s2[r:r+len(s1)]
                # this is O(m)
                while l <(len(s1)):
                    # this is O(m)
                    if s1[l] not in  new_String:
                        res = res and False
                        break
                    else:
                        # this is O(m)
                        new_String =  new_String.replace(s1[l],"",1)
                    l+=1
                if res:
                    return res

            r+=1
        # total time complexity is O(n) * [O(m)+O(m)*(O(m)+O(m))]=>O(n*m^2)
        # space complexity is O(m)
        return False


    # here the complexity is T = > O(m+n) due to sliding window
    # S => O(1) as the space is O(26) regardless of the input size.
    def checkInclusion_single_window(self, s1: str, s2: str) -> bool:
        # if  the substring is greater then already false
        if len(s1)>len(s2):
            return False
        countS1 = [0]*26
        countS2 = [0]*26
        # create a counter of characters of first window of s2
        ''' the window is of length s1 so only updating the value
        of the characters from window from 1 to len(s1)
        '''
        for i in range(len(s1)):
            countS2[ord(s2[i])-ord('a')]+=1
            countS1[ord(s1[i])-ord('a')]+=1
        matches = 0
        '''calculate the matches of characters, in a window it matches means
        it contains permutations
        If I have used the hasmap for counting then the space requirement
        would be of O(len(s1))
        So to use O(1) the contant memory is utilized'''
        for i in range(26):
            matches+=(1 if countS1[i]==countS2[i] else 0)
        print("counts",countS2)
        print("matches",matches)
        # initlializing the start of window
        l  = 0
        # iteration will go from len(s1) to end of s2 .
        # this is the end value of the window which goes till end of s2
        for r in range(len(s1),len(s2)):
            # check value of matches for every iterations
            if matches == 26:
                return True
            # adding a new character to the window.
            index = ord(s2[r])-ord('a')
            countS2[index] +=1
            # if the new value of count of that character matches then
            # match number is increased
            if countS1[index]==countS2[index]:
                matches+=1
            # if after increasing the count the count of character in s2
            # is greater than in s1 this is mismatch
            elif countS1[index]+1==countS2[index]:
                matches-=1
            print("add",matches,countS2)
            index = ord(s2[l])- ord('a')
            countS2[index] -=1
            # if the new value of count of that character matches then
            # match number is increased
            if countS1[index]==countS2[index]:
                matches+=1
            # if after increasing the count the count of character in s2
            # is greater than in s1 this is mismatch
            elif countS1[index]-1==countS2[index]:
                matches-=1
            print("sub",matches,countS2)
            # move the window by a single character
            l+=1
        return matches==26


eval = Solution()
out1 = eval.checkInclusion(s1,s2)
print(out1)

out2 = eval.checkInclusion_window(s1,s2)
print(out2)

out3 = eval.checkInclusion_window_optimal(s1,s2)
print(out3)


out5 = eval.checkInclusion_single_window(s1,s2)
print(out5)
