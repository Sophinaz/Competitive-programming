class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        pas = 0
        pos = 0
        l,r = 0,0
        result = 0
        while r < len(answerKey):
            if answerKey[r] == 'F':
                if pas<k:
                    pas+=1
                else:
                    result = max(result,r-l)
                    l =r
                    pas -=1 
                r+=1
            else:
                r+=1
        l,r,pas = 0,0,0
        while r < len(answerKey):
            if answerKey[r] == 'T':
                if pas<k:
                    pas+=1
                else:
                    result = max(result,r-l)
                    l =r
                    pas -=1 
                r+=1
            else:
                r+=1
        if len(answerKey) != 0 and result == 0:
            return len(answerKey)
        return result
                