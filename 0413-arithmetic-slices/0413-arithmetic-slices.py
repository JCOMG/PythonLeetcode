class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        l = []
        a = 1
        count = 0
        current_streak = 0

        if len(nums) <= 1:
            return 0

        if len(nums) == 2:
            if nums[0] == nums[1]:
                return 1
            else:
                return 0

        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                # 增加當前等差序列的長度
                current_streak += 1
                # 更新總計數
                count += current_streak
            else:
                # 如果不符合等差條件，重置當前等差序列長度
                current_streak = 0
        return count
