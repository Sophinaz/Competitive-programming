class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        cap = capacity
        result = 0
        for i in range(len(plants)):
            if capacity < plants[i]:
                result += ((i + 1) * 2) - 1
                capacity = cap - plants[i]
            else:
                result += 1
                capacity -= plants[i]

        return result