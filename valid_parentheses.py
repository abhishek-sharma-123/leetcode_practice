#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#An input string is valid if:
#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
 
 
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i=="(" or i=="[" or i=="{":
                stack.append(i)
            elif i==")" or i=="]" or i=="}":
                if len(stack)==0:
                    return False
                else:
                    if i==")":
                        if stack[-1]=="(":
                            stack.pop()
                        else:
                            return False
                    elif i=="]":
                        if stack[-1]=="[":
                            stack.pop()
                        else:
                            return False
                    if i=="}":
                        if stack[-1]=="{":
                            stack.pop()
                        else:
                            return False
        if len(stack)==0:
            return True
        else:
            return False
                         