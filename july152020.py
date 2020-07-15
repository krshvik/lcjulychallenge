class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split()
        ts = ''
        lena = len(a)-1
        while lena > -1:
            ts = ts + a[lena]
            lena = lena-1
            if lena >-1:
                ts = ts + ' '
        return ts 