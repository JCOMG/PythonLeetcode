class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # use Two pointers
        if len(nums) <= 2:
            return len(nums)

        index = 2  # maximum duplicate element is 2

        for i in range(2,len(nums)):#處理前兩個元素時，不需要進行任何動作，因為無論這兩個元素是否相同，我們都可以保留它們。
            if nums[i] != nums[index - 2]:  # make sure not the same as the previous one
                nums[index] = nums[i]
                index += 1
            else:
                continue
        return index
        
        