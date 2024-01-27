class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        result = 0
        t = 0
        count[0] = 1
        for i in nums:
            t+=i
            n = t % k
        
            result += count[n]
            count[n] += 1
            
        return result