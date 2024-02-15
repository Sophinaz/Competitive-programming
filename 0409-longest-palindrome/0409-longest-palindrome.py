class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        result = 0
        check = True
        for i in count:
             
            if count[i] % 2 == 0 and count[i] :
                result += count[i]
            else: 
                result += count[i] -1
                count[i] = 1
            
            if count[i] == 1 and check: 
                result += 1
                check = False

        return result 