class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        
        for i in image:
            i[:] = i[::-1]
            for j in range(m):
                if i[j] == 1: i[j] = 0
                else: i[j] = 1

        return image 