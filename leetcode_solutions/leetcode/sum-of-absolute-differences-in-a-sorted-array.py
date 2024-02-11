class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]
        answer = [0] * n
        for i in range(1,n):
            prefix[i] = nums[i] + prefix[i-1]
        print(prefix)
        for i in range(n):
            before = 0
            if i > 0:
                before = (nums[i]*i) - prefix[i-1]

            after = (prefix[n-1] - prefix[i]) - (nums[i] * (n-i-1))

            answer[i] = before + after
        return answer