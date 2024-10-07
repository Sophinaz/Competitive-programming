class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        def checker(l1, l2):
            if len(l1) != len(l2):
                return False
            for i in range(len(l1)):
                if l1[i] != l2[i]:
                    return False
            return True

        sen1, sen2 = sentence1.split(), sentence2.split()
        if len(sen2) > len(sen1):
            sen1, sen2 = sen2, sen1
        i = 0
        while i < len(sen2) and sen1[i] == sen2[i]:
            i += 1
        if i == len(sen2): return True

        res = False
        for j in range(i+1, len(sen1)):
            if sen1[j] == sen2[i]:
                res = checker(sen1[j+1:], sen2[i+1:]) 

        if not res:
            return sen1[len(sen1)-len(sen2): ] == sen2
        else:
            return res