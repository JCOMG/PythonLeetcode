class Solution:
    def minimumSum(self, num: int) -> int:
        # 因為有重複的值，我們可以直接 sort，從小排到大
        # 如果值是 2932且我們假設值的長度是 len(num) == 4 ，
        # 有兩個 2 sort完之，變成 2 2 3 9 ，第一個 2 跟 3 配對，第二個 2 跟 9 配對
        num_str = list(str(num))
        num_sorted  = sorted(num_str)
        print(num_sorted)
        return int(num_sorted[0]+num_sorted[2]) + int(num_sorted[1] + num_sorted[3])