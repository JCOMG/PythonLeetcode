class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for i in strs:
            after_sorted = str(sorted(i))
            
            if after_sorted not in dictionary:
                dictionary[after_sorted] = [i]
                # 這裡的意思界是說 把 ['a', 'e', 't'] 變成 key , 然後值是 eat, 一定要加中括號因為要把它變成 List , 後面append 要用
                # -> { ['a', 'e', 't'] : ['eat'] }
            else:
                dictionary[after_sorted].append(i)
                # 如果有重複的話，直接append在原本的 value 的後面
                # -> { ['a', 'e', 't'] : ['eat' , 'tea']}
        return list(dictionary.values())
        # return 回去 我們的 dictionary 的值 ，但是，題目要求我們也要將返回的值加個 list 
        # 所以變成 -> [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]