class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        count1 = 0
        ANSWER = 0
        for i in s:
            # print(i)
            if i == "R":
                count += 1
            elif i == "L":
                count1 += 1

            if count == count1:# 次數一樣，代表就是 1 組
               # 重新設置 R、L的次數
                count = 0
                count1 = 0
                ANSWER += 1
        return ANSWER