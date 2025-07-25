class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        result = [row[:] for row in img]
        n_row = len(img)
        n_col = len(img[0])
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1], [1, 1], [-1, 1], [-1, -1], [1, -1]]
        def valid(row, col):
            return 0 <= row < len(img) and 0 <= col < len(img[0])

        for row in range(n_row):
            for col in range(n_col):
                count = 1
                total = img[row][col]
                for r, c in directions:
                    new_row = row + r
                    new_col = col + c
                    if valid(new_row, new_col):
                        count += 1
                        total += img[new_row][new_col]
                result[row][col] = total // count

        return result