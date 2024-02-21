class Solution:
    def reverseString(self, s: List[str]) -> None:
        # answer = [0] * len(s)
        self.i = 0
        def reverse (s,idx):
            if idx == len(s) - 1:
                s[self.i] = s[-1]
                self.i+=1
                return s[-1]
            
            letter = s[idx]
            t = reverse(s,idx + 1)
            s[self.i] = letter
            self.i+=1
            return s
        return reverse(s,0)
