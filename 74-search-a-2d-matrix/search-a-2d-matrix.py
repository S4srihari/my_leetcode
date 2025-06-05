class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix)-1

        while top <= bot:
            mid = (top + bot)//2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                top = mid + 1
            else:
                bot = mid - 1

            left,right = 0, len(matrix[0])-1
            while left <= right:
                mid2 = (left + right)//2
                if matrix[mid][mid2] == target:
                    return True
                elif matrix[mid][mid2] < target:
                    left = mid2+1
                else :
                    right = mid2-1
        return False