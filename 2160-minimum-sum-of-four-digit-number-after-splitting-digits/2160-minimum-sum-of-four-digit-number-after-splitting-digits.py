class Solution:
    def minimumSum(self, num: int) -> int:
        l = []
        num = str(num)
        # print(num)
        for i in num:
            l.append(i)

        l = sorted(l)
        # print(l)

        return int(l[0] + l[2]) + int(l[1] + l[3])

