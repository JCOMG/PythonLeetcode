class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums) ):
                if nums[j] != nums[i]:
                    continue
                elif nums[j] == nums[i]:
                    count += 1
                else:
                    return 0
        return count