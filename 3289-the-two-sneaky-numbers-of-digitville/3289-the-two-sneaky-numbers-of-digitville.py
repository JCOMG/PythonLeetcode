class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        l = []
        for i in range(len(nums)):
            counting = nums.count(nums[i])
            if counting == 1:
                continue
            if nums.count(nums[i]) > 1:
                if nums[i] in l:
                    continue
                else:
                    l.append(nums[i])
        return l