class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        # perform XOR using ^ operator
        sum = 0
        l = []
        l.append(pref[0])
        for i in range(len(pref)):
            if len(pref) <= 1:
                return [pref[i]]
            else:
                j = i + 1
                if j < len(pref):
                    sum = pref[i] ^ pref[j]
                    l.append(sum)

        return l
        