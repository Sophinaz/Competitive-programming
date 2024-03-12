class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = [0] * n
        idx = 0

        for num in range(1,n+1):
            if num % 3 == 0 and num % 5 == 0:
                result[idx] = "FizzBuzz"
            elif num % 3 == 0:
                result[idx] = 'Fizz'
            elif num % 5 == 0:
                result[idx] = 'Buzz'
            else:
                result[idx] = str(num)
            idx += 1

        return result