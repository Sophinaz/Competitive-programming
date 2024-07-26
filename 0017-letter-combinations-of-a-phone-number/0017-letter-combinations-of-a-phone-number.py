class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        track = {2: ['a','b','c'], 3: ['d','e','f'], 4: ['g','h','i'],
                    5: ['j','k','l'],6: ['m','n','o'],7: ['p','q','r','s'],
                    8: ['t','u','v'],9: ['w','x','y','z'] }
        result = []
        if not digits: return result
        
        def backtrack(idx,path):
            if len(path) == len(digits):
                result.append(''.join(path))
                return
            n = int(digits[idx])
            for i in range(len(track[n])):
                path.append(track[n][i])
                backtrack(idx + 1,path)
                path.pop()

        backtrack(0,[])
        return result
