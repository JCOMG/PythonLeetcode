class Solution:
    def clearDigits(self, s: str) -> str:
        i = 0
        while i < len(s):
            if not s[i].isdigit():
                i = i + 1
                continue
            if s[i].isdigit():
                if i > 0:
                    s = s[:i - 1] + s[i + 1:]
                    i = i - 1  # Adjust index after removing two characters
                    continue
                else:
                    s = s[i + 1:]  # maybe the first letter is digital
            i = i + 1
        return s