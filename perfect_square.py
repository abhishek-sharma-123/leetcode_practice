#Given a positive integer num, write a function which returns True if num is a perfect square else False.
#Follow up: Do not use any built-in library function such as sqrt.

import math
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==1:
            return True
        r=int(math.sqrt(num))
        def sq(num):
            if num>=r:
                return sq(num/r)
            elif num==1.0:
                return True
            else:
                return False
        return sq(num)