#An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

#Given an integer n, return true if n is an ugly number.

 

class Solution:
    def isUgly(self, n: int) -> bool:
        while n!=1.0:
            if n%2==0:
                n=n/2
            else:
                if n%3==0:
                    n=n/3
                else:
                    n=n/5
            if n<1:
                return False
        return True