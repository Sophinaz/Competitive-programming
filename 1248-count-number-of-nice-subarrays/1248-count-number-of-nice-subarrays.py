class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l,r = 0,0
        count,even,result = 0,0,0
        track = {0:1}
        n=len(nums)
        for i in range(len(nums)):
            if nums[i] %2 != 0:
                nums[i] = 1
            else: nums[i] = 0
        print(nums)
        for i in nums:
            count+=i
            t = count-k
            if t in track:
                result += track[t]
                
            if count in track: track[count] +=1
            else: track[count] = 1
        print(track)
        return result
                
                
        