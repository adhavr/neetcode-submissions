class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        while r >= l:
            mid = (r + l) // 2

            if matrix[mid][0] <= target:
                if target in matrix[mid]:
                    return True
                l = mid + 1
            else:
                r = mid - 1
        return False