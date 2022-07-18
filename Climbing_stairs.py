#You are climbing a staircase. It takes n steps to reach the top.

#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


class Solution:
    def climbStairs(self, n: int) -> int:
        list1 = [1,1]
        for i in range(1,45):
            list1.append(list1[i] + list1[i-1])
        return list1[n]
            