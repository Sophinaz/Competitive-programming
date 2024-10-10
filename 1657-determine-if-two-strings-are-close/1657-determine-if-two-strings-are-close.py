class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1 = sorted(list(word1))
        word2 = sorted(list(word2))
        if word1 == word2:
            return True
        if len(word1) != len(word2):
            return

        count1 = Counter(word1)
        count2 = Counter(word2)
        count = Counter(count2.values())

        removed = 0
        for i in count1:
            if i not in count2:
                return
            if count[count1[i]] > 0:
                count[count1[i]] -= 1

            removed += 1

        return removed == len(count1) and sum(count.values()) == 0 