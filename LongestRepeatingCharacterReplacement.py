s = "XXYABXX";
k = 2


class Solution:
    #sliding window
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        store = set(s)
        for c  in store:
            count = l  = 0
            for j in range(len(s)):
                if(s[j]==c):
                    count+=1
                while (j-l+1)-count > k:
                    if s[l]==c :
                        count-=1
                    l+=1
                res = max(res,j-l+1)

        return res
    # The principle of sliding window here is
    # l is the starting value of  the window to track the start
    # r is the end of the window .
    # the length of the window for a character is done by adding k .
    # if there are more of same characters after k characters then it makes
    # sense to add , but if there are none then count is increased and the
    # starting value l is increased to start of new character
    # sliding window
    def characterReplacement_optimal(self, s: str, k: int) -> int:
        res = 0
        store = {}
        l = 0
        maxf = 0
        for r  in range(len(s)):
            store[s[r]] = 1+ store.get(s[r],0)
            maxf = max(maxf,store[s[r]])
            print(maxf,store)
            while (r-l+1) - maxf > k:
                store[s[l]]-=1
                l+=1
            res = max(res,r-l+1)

        return res


eval = Solution()
out1 = eval.characterReplacement(s,k)
print(out1)

out2 = eval.characterReplacement_optimal(s,k)
print(out2)
