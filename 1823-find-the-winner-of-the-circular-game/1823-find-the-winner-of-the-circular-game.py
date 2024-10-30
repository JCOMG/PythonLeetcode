class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l = []
        for i in range(n):
            l.append(i + 1)

        j = 0
        while len(l) > 1:  # we have to leave one friend
            j = (j + k - 1) % len(l)

            l.remove(l[j])

        return l[0]
        