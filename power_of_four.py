#Given an integer n, return true if it is a power of four. Otherwise, return false.

#An integer n is a power of four, if there exists an integer x such that n == 4x.

 

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def power(n):
            if n>=4:
                return power(n/4)
            elif n==1.0:
                return True
            else:
                return False
        return power(n)