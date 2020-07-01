class Solution:
    def arrangeCoins(self, n: int) -> int:
        tote = 0 
        i = 0
        while tote + i + 1 <= n:
            tote = tote + i
            if tote + i + 1 <= n:
                i = i + 1
            else:
                return i 
        return i 