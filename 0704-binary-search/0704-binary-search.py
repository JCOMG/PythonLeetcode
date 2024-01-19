class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1
        # medium = (L + R) // 2  這個放在 for 迴圈外免會導致 每次計算只能算出 固定的 L、R 都沒有更新，所以會跑出 TLE
        while L <= R:
            medium = (L + R) // 2  # 整除
            if nums[medium] < target:
                L = medium + 1
            elif nums[medium] > target:
                R = medium - 1
            elif nums[medium] == target:
                return medium
        return -1
        