class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {}
        l,r = 0,0
        result = 0
        n = len(s)
        while r <= n:
            if r == n:
                print('a',r,l) 
                result = max(result,r-l)
                break
            if s[r] not in count: count[s[r]] =1
            else:
                count[s[r]] += 1
                if count[s[r]] > 1:
                    result = max(result,r-l)
                    while count[s[r]] > 1:
                        count[s[l]]-=1
                        l+=1
            r+=1
        return result
                    
