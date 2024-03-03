class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        # requests.sort(key = lambda x: x[1])
        nums.sort(reverse = True)
        num = requests[-1][1]
        numbers = [0] * (len(nums)+1)
        result = 0
        
        for i,j in requests:
            numbers[i] += 1
            if j < len(numbers)-1: numbers[j+1] -= 1 
        
        for i in range(1,len(numbers)):
            numbers[i] = numbers[i-1] + numbers[i]
        numbers.sort(reverse = True)
       
        for i in range(len(nums)):
            result += (numbers[i] * nums[i]) 

        return result % ((10 ** 9)+7)

