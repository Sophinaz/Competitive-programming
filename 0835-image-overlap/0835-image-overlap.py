class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        overlap = defaultdict(int)

        def calculate_overlap(row, col):
            for row_2 in range(len(img2)):
                for col_2 in range(len(img2[0])):
                    if img2[row_2][col_2]:
                        difference = (row - row_2, col - col_2)
                        overlap[difference] += 1


        for row in range(len(img1)):
            for col in range(len(img1[0])):
                if img1[row][col]:
                    calculate_overlap(row, col)

        return max(list(overlap.values())) if len(overlap) else 0