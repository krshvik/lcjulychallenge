class Solution:
    def addBinary(self, a: str, b: str) -> str:
        while len(a) < len(b):
            a = '0' + a
        while len(b) < len(a):
            b = '0' + b
        
        ts = ''
        lenb =len(b)-1
        carry = '0'
        while lenb > -1:
            ai = a[lenb:lenb+1]
            bi = b[lenb:lenb+1]
            
            ci = self.bina(ai,bi)
            c2i = self.bina(ci,carry)
            
            if len(c2i) > 1:
                carry = '1'
                ts = c2i[1:] + ts
            else:
                carry = '0'
                ts = c2i + ts
            
            lenb = lenb-1
        
        if carry == '1':
            ts  = carry + ts 
        return ts 
            
    def bina(self,s1,s2):
        
        if s1 == '0':
            return s2
        
        if s2 == '0':
            return s1
        
        
        if s1 == '1':
            if s2 == '1':
                return '10'
            return '11'
        
        if s2 == '1':
            if s1 == '1':
                return '10'
            return '11'