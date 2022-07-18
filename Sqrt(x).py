class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 :
            return 0
        elif x == 1:
            return 1
        else:
            for i in range(1,x//2 + 1):
                if x >= i*i and x < (i+1)*(i+1):
                    return i