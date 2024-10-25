class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        length = len(s)
        for i in range(length - 2):  # make sure the window is smaller than the len(s)
            window = s[i:i + 3]  # get the window's length = 3
            if len(set(window)) == 3: # calculate the window's string
                count += 1
        return count
        