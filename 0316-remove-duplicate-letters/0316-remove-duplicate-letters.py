class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        l = []
        stack = []

        for i in range(len(s)):
            for i, char in enumerate(s):
                #                 for example:
                #                 i   char
                #                 0    c
                #                 1    b
                #                 2    a
                #                 3    c  and so on 

                if char in stack:
                    continue
                    

                while stack and stack[-1] > char and stack[-1] in s[i:]:
                    # check if the stack is empty or not (while stack)
                    # check the top of the stack is bigger than the char
                    # foe example if it is b coming, stack only has 'c' (stack[-1] > char)
                    # so we can just check is 'c' > 'b' is the same as ord(c) > ord(b)
                    # we can check if the top character in stack still in the s
                    # if still in the s, we can pop it cause we will see it again 
                    
                    stack.pop()

                stack.append(char)

            x = "".join(stack)
            return x

        