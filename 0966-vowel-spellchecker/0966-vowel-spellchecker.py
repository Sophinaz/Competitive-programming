class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def makeLowerCaseWord(word):
            new_word = []
            for c in word:
                if c in vowels:
                    new_word.append(".")
                else:
                    new_word.append(c.lower())
            return "".join(new_word)
            
        vowels = "aeiouAEIOU"
        spellMapExact = {}
        spellMapCapitilization = {}
        spellMapVowels = {}
        answer = []

        for i in range(len(wordlist)):
            word = wordlist[i]
            new_word = makeLowerCaseWord(word)
            if word not in spellMapExact:
                spellMapExact[word] = i
            if word.lower() not in spellMapCapitilization:
                spellMapCapitilization[word.lower()] = i
            if new_word not in spellMapVowels:
                spellMapVowels[new_word] = i                


        for i in range(len(queries)):
            word = queries[i]
            check_word = makeLowerCaseWord(word)
            
            if word in spellMapExact:
                answer.append(wordlist[spellMapExact[word]])
            elif word.lower() in spellMapCapitilization:
                answer.append(wordlist[spellMapCapitilization[word.lower()]])
            elif check_word in spellMapVowels:
                answer.append(wordlist[spellMapVowels[check_word]])
            else:
                answer.append("")

        return answer