class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        print(output)
        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):  # 起點是 len(nums) - 1 , 結束點是 - 1 但會自動 + 1 , 再 -1 遞減
            output[i] *= postfix # 要乘以 我們剛剛 所 儲存的 prefix
            postfix *= nums[i]
        return output