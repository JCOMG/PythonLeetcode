class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            windows = nums[i + 1:i + k + 1]
            if nums[i] in windows:
                return True
        return False
        