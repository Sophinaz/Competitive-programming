class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        result = 0
        left,right = 1,len(skill)-2
        while left < right:
            if skill[left-1] + skill[right +1] != skill[left] + skill[right]:
                return -1
            result += skill[left-1] * skill[right + 1]

            left += 1
            right -= 1
        return result + skill[left-1] * skill[right + 1]
