class Solution:
    def reverseBits(self, n: int) -> int:
        n2 = str(bin(n))[2:]
        while len(n2) < 32:
            n2 = '0' + n2
        return int(n2[::-1],2)