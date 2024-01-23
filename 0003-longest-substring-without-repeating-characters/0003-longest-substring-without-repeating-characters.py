class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = defaultdict(int)
        result = 0
        l,r=0,0
        while r<len(s) and l<=r:
            print(count)
            print(count[s[r]])
            if count[s[r]] == 1:
                print(s[r])
                # print(count)
                result = max(result,r-l)
                while count[s[r]]==1:
                    count[s[l]] -= 1
                    l+=1
            else:
                count[s[r]] +=1
                r+=1
        return result

        