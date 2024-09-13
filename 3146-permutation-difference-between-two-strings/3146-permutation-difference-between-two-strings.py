class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        sum = 0
        dict_s = {}
        dict_t = {}
        for i in range(len(s)):
            index_s = s[i]  # 以 s = "abcde" 為例, key = a = s[i]
            dict_s[index_s] = i  # value = 0 = i, dict_s ={ 'a':0 }

            # key  value
            #  a     0
            #  b     1
            #  c     2
            #  d     3
            #  e     4

        for j in range(len(t)):
            index_t = t[j]  # 以 t = "edbac" 為例, key = e = t[j]
            dict_t[index_t] = j # value = 0 = j,  dict_t ={ 'e':0 }

            # key  value
            #  e     0
            #  d     1
            #  b     2
            #  a     3
            #  c     4

        for char in s:
            sum += abs(dict_s[char] - dict_t[char])
        return sum
        
        