class Solution:
    def smallestNumber(self, num: int) -> int:
        negative = False
        result = ""
        if str(num)[0] == '-':
            negative = True
            num = list(str(num))
            num = num[1:]
        else: num = list(str(num))
        if not negative:
            num[:] = sorted(num[:])
            i = 1
            while num[0] == '0' and i<len(num):
                num[0],num[i] = num[i],num[0]
                i+=1
        else:
            num[:] = sorted(num[:],reverse=True)
        if negative:result += '-'
        for i in num:
            result+=str(i)
        return int(result)

                