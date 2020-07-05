class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x1 = str(bin(x))[2:]
        y1 = str(bin(y))[2:]
        
        if len(x1) == len(y1):
            t = 0 
            while len(x1) > 0:
                if x1[:1] != y1[:1]:
                    t = t + 1
                x1 = x1[1:]
                y1 = y1[1:]
            return t
        
        while len(x1) < len(y1):
            x1 = '0' + x1
        while len(y1) < len(x1):
            y1 = '0' + y1
        t = 0 
        while len(x1) > 0:
            if x1[:1] != y1[:1]:
                t = t + 1
            x1 = x1[1:]
            y1 = y1[1:]
        return t 
                    