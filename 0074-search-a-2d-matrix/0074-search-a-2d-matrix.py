class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(0, len(matrix)):
            L = 0
            R = len(matrix[i])-1
            while L <= R:
                medium = (L + R) // 2
                if matrix[i][medium] == target:
                    return True
                if medium < len(matrix[i]) - 1 and matrix[i][medium] < target:
                    L = medium + 1
                elif medium < len(matrix[i]) - 1 and matrix[i][medium] > target:
                    R = medium - 1
                elif medium < len(matrix[i]) - 1 and matrix[i][medium] == target:
                    return True
                else:
                    break
        return False