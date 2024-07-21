class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        print(not nums)
        if not nums:
            return 0
        nums = set(nums)
        current = 0
        current_length = 0
        max_length = 0
        for i in nums:
            if i - 1 not in nums:  # 代表前面沒有數字，所以沒有連續，所以可以定義為 起始點
                current = i
                current_length = 1
            while current + 1 in nums:
                current += 1
                current_length += 1
            if current_length > max_length:
                max_length = current_length
        return max_length
        