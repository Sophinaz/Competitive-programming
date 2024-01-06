class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s[::-1]
        s = list(s.split())
        result = ""
        for i in range(len(s)):
            if i != len(s)-1:
                result += s[i][::-1] + " "
            else:
                result += s[i][::-1]
        
        return result 
            

        