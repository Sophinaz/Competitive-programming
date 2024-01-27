class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        result = 0
        pre = 0
        for i in nums:
            pre += i
            result += count.get(pre - k, 0)
            count[pre] += 1
        return result
