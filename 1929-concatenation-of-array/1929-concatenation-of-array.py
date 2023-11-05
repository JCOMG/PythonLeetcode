class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        list = []
        list1 = []
        for i in nums:
            list.append(i)
            # print (list)
        return list*2
        
        