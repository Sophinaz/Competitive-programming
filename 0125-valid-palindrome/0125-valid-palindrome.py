class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s1 = ''
        s = s.lower
        for c in s:
            if c.isalnum():
                s1 += c

        return True if s1==s1[::-1] else False