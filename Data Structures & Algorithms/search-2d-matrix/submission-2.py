class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        numrows = len(matrix)
        numcols = len(matrix[0])

        t,b = 0,numrows - 1
        while t <= b:
            middle = (t+b) // 2

            if matrix[middle][-1] < target:
                t = middle + 1
            elif matrix[middle][0] > target:
                b = middle - 1
            else:
                break
        if not (t <= b):
            return False
        
        row = (t+b) // 2 
        l,r = 0, numcols - 1
        while l <= r:
            m = (l+r) // 2
            if target > matrix[row][m]:
                l = m+1
            elif target < matrix[row][m]:
                r = m - 1
            else: 
                return True

        return False