class Solution:
    def convertDateToBinary(self, date: str) -> str:
        count = 0
        sum = 0
        date = date.replace("-", "")
        for i in date:
            date_number_1 = int(date[:4])
            date_number_bin_1 = bin(date_number_1)[2:]
            date_number_2 = int(date[4:6])
            date_number_bin_2 = bin(date_number_2)[2:]
            date_number_3 = int(date[6:8])
            date_number_bin_3 = bin(date_number_3)[2:]
            date_bin = date_number_bin_1 + "-" + date_number_bin_2 + "-" + date_number_bin_3
        return date_bin


if __name__ == '__main__':
    solution = Solution()
    result = solution.convertDateToBinary("2100-02-31")
    print(result)
