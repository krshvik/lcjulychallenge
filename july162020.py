class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x 
        if n == 0:
            return 1
        res = x 
        sign = 1
        if n < 0:
            n = n*-1
            sign = sign*-1
        i = 1
        while (i*2) < n:
            res = res*res
            i = i * 2 
        val = res*self.myPow(x,n-i)
        
        if sign == -1:
            return 1/val
        return val       