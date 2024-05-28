class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            # 將字串排序後作為鍵
            sorted_str = " ".join(sorted(s))  # 將 " " 這個空格加入sorted s 的 「後面」 
            print(sorted_str)
            # 如果鍵不存在，則新增一個空清單
            if sorted_str not in dic:
                dic[sorted_str] = []  # aet :[]

            # 將字串添加到對應的鍵的清單中
            dic[sorted_str].append(s)  # aet : ["eat",'tea', 'ate'] , ant : ['tan', 'nat'] ,abt : ['bat']

        # 將字典中的值轉換為包含這些清單的清單
        return list(dic.values())  # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]