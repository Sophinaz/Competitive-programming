class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse = True)
        count = 0
        result = 0
        i = 0
        left,right = 0,len(people)-1
        while left <= right:
            if people[left] + people[right] <= limit:
                right -= 1
            left += 1
            result += 1
        return result 
                