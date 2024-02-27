class Solution:
    def countGoodNumbers(self, n: int) -> int:
        if n % 2: odd = True
        else: odd = False
        if n == 1: return 5
        n //= 2

        def countgood(n):
            if n == 1: return 20
            temp = (countgood(n//2)) % ((10 ** 9) + 7)
            if n % 2 == 0: return temp * temp
            else: return temp * temp * 20
        if odd: return countgood(n) * 5 % ((10 ** 9) + 7)
        else: return countgood(n) % ((10 ** 9) + 7)