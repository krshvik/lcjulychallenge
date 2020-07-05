class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x1 = str(bin(x))[2:]
        y1 = str(bin(y))[2:]
        
        t = 0 
        
        while len(x1) < len(y1):
            if y1[:1] == '1':
                t = t + 1
            y1 = y1[1:]

        while len(y1) < len(x1):
            if x1[:1] == '1':
                t = t + 1
            x1 = x1[1:]

        while len(x1) > 0:
            if x1[:1] != y1[:1]:
                t = t + 1
            x1 = x1[1:]
            y1 = y1[1:]
        return t                     