class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l1 = []
        l2 = []
        i = 0
        for i in range(0, n):
            l1.append(nums[i])
            for n in range(n, len(nums)):
                l1.append(nums[n])
                n = n + 1
                break
        return l1
        