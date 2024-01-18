class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if i < j and nums[i] + nums[j] < target:
                    count += 1
                else:
                    continue
        return count