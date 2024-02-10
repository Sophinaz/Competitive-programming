class Solution:
    def numberOfWays(self, s: str) -> int:
        track = {}
        prefix,result,left = 0,0,0
        
        num0post = s.count('0')
        num1post = s.count('1')
        num0pre,num1pre = 0,0

        for i in s:
            if i == '0':
                result += num1pre * (num1post-num1pre)
                num0pre += 1
            else:
                result += num0pre * (num0post-num0pre)
                num1pre += 1
        
        return result


