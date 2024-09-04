class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        result = []
        for word in words:
            if len(word) != len(pattern):
                continue
            check = defaultdict(chr)
            check1 = defaultdict(chr)
            flag = True
            
            for i in range(len(word)):
                if word[i] in check and check[word[i]] != pattern[i]:
                    flag = False
                    break
                elif pattern[i] in check1 and check1[pattern[i]] != word[i]:
                    flag = False
                    break
                else:
                    check[word[i]] = pattern[i] 
                    check1[pattern[i]] = word[i]
            if flag: result.append(word)
        return result