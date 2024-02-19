class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        s = list(palindrome)
        if len(s) == 1: return ""
        count  = Counter(palindrome)
        flag = False
        for i in range(len(s)):
            if len(s) %2!= 0 and i == len(s) // 2 :
                if len(count) == 2 and count[s[i]] == 1:
                    continue
            
            if s[i] != 'a':
                s[i] = 'a'
                flag = True
                break
        
        if not flag and len(s) > 1: 
            s[-1] = 'b'
            flag = True
        

        if flag: return "".join(s)
        else: return ""