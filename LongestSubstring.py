s = "xxddfferds"
class Solution:
    #using array : my solution
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        store = []
        for r in s:
            if(r in store):
                store = store[store.index(r)+1:]
            store.append(r)
            res = max(res,len(store))


        return res
    #using set
    def lengthOfLongestSubstring_set(self, s: str) -> int:
        res = 0
        store = set()
        l = 0
        for r in range(len(s)):
            while s[r] in store:
                print(store,s[r],s[l],l)
                store.remove(s[l])
                l+=1
            store.add(s[r])
            res = max(res,r-l+1)

        return res
    # using sliding window
    def lengthOfLongestSubstring_sliding_window(self, s: str) -> int:
        res = 0
        store = {}
        l = 0
        for r in range(len(s)):
            if s[r] in store:
                l = max(store[s[r]]+1,l)
            store[s[r]] = r
            print(r,l)
            print(store)
            res = max(res,r-l+1)
        return res




eval = Solution();
out1 = eval.lengthOfLongestSubstring(s)
print(out1)

out2 = eval.lengthOfLongestSubstring_set(s)
print("second",out2)

out3 = eval.lengthOfLongestSubstring_sliding_window(s)
print("third",out3)
