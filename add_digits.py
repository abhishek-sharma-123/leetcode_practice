#Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

class Solution:
    def addDigits(self, num: int) -> int:
        while True:
            num=str(num)
            list1=[int(i) for i in num]
            add=sum(list1)
            add=str(add)
            if len(add)==1:
                return int(add)
            num=add