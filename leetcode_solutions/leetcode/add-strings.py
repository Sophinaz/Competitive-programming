class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        left, right = len(num1)-1, len(num2)-1
        result = deque()
        carry = 0

        while left > -1 and right > -1:
            num = int(num1[left]) + int(num2[right]) + carry
            carry = 0
            if num > 9:
                num = str(num)
                result.appendleft(num[1])
                carry = int(num[0])
            else:
                result.appendleft(str(num))
            
            left -= 1
            right -= 1
        ptr = -1
        
        if left > -1: 
            nums = num1
            ptr = left
        elif right > -1: 
            nums = num2
            ptr = right

        while ptr > -1:
            num =  int(nums[ptr]) + carry
            carry = 0
            if num > 9:
                num = str(num)
                result.appendleft(num[1])
                carry = int(num[0])
            else:
                result.appendleft(str(num))
            ptr -= 1 
        if carry > 0: result.appendleft(str(carry))

        return ''.join(result)


