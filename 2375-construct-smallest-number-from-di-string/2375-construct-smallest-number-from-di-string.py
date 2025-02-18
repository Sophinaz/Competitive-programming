class Solution:
    def smallestNumber(self, pattern: str) -> str:
        def backtrack(i, check, number):
            if i == len(pattern):
                return number

            for num in range(1, 10):
                if pattern[i] == 'D' and num < number[-1] and num not in check:
                    check.add(num)
                    number.append(num)
                    x = backtrack(i+1, check, number)
                    if x:
                        return x
                    if num in check: check.remove(num)
                    number.pop()
                elif pattern[i] == 'I' and num > number[-1] and num not in check:
                    check.add(num)
                    number.append(num)
                    x = backtrack(i+1, check, number)
                    if x:
                        return x
                    if num in check: check.remove(num)
                    number.pop()

        for i in range(1, 10):
            x = backtrack(0, set([i]), [i])
            if x:
                res = ''.join([str(i) for i in x])
                return res
