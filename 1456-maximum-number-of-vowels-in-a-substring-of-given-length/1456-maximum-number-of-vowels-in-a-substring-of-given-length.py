class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        result,total = 0,0
        for i in range(k):
            if s[i] in vowels:
                total += 1
        
        left = 0
        result = max(result,total)
        
        for right in range(k,len(s)):
            if s[right] in vowels: total += 1
            
            if s[left] in vowels: total -= 1
            left += 1
            result = max(result,total)

        return result 

