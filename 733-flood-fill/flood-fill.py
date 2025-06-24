class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start = (sr,sc)
        pcolor = image[sr][sc]
        if pcolor == color: return image
        m, n = len(image), len(image[0])
        q = []
        q.append(start)
        while q:
            pos = q.pop(0)
            image[pos[0]][pos[1]] = color
            for x,y in [(pos[0]+1,pos[1]), (pos[0]-1,pos[1]), (pos[0],pos[1]+1), (pos[0],pos[1]-1)]:
                if 0 <= x < m and 0<= y < n and image[x][y] == pcolor :
                    image[x][y] = color
                    q.append((x,y))
        return image