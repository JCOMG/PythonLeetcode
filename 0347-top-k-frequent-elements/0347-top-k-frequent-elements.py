class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)):
            if sorted_nums[i] not in dictionary:
                count = 1
                dictionary[sorted_nums[i]] = count
            else:
                count = count + 1
                dictionary[sorted_nums[i]] = count
        
        k_list = []
        for j in range(k):
            maximum = max(dictionary, key = dictionary.get)
            k_list.append(maximum)
            del dictionary[maximum]
        return k_list