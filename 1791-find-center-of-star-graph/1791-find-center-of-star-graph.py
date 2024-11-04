class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        l = []
        for i in range(len(edges)):
            for j in range(len(edges[i])):
                if edges[i][j] not in l:
                    l.append(edges[i][j])
                else:
                    return edges[i][j]
        