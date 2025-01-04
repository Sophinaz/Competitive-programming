class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = "aeiou"
        prefix = [0 for i in range(len(words))]
        result = []

        for i in range(len(words)):
            word = words[i]
            if word[0] in vowels and word[-1] in vowels:
                prefix[i] += 1

        for i in range(1, len(prefix)):
            prefix[i] += prefix[i-1]

        for start, end in queries:
            if start > 0:
                result.append(prefix[end] - prefix[start-1])
            else:
                result.append(prefix[end])

        return result