class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        track = {0:1}
        prefix,result = 0,0
        for i in nums:
            prefix += i
            

            if prefix - k in track: 
                result += track[prefix-k]

            track[prefix] = 1 + track.get(prefix,0)

        return result