class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        di = {}
        ov = {}
        ov[0] = 1
        ov[2] = 1 
        cs = ''
        while N > 0 :
            arr = [0]
            i = 1 
            cs = '0'
            while i <= 6:
                if cells[i-1] + cells[i+1] in ov:
                    arr.append(1)
                    cs = cs + '1'
                else:
                    arr.append(0)
                    cs = cs + '0'
                i = i + 1
            arr.append(0)
            N = N - 1 
            cells = arr 
            cs = cs + '0'            
            
            if cs not in di:
                di[cs] = 1 
            else:
                break
                
        if N == 0:
            return cells 
        
        di = {}
        ret = []
        cs = ''
        while N > 0 :
            arr = [0]
            i = 1
            cs = '0'
            while i <= 6:
                if cells[i-1] + cells[i+1] in ov:
                    arr.append(1)
                    cs = cs + '1'
                else:
                    arr.append(0)
                    cs = cs + '0'
                i = i + 1
            arr.append(0)
            cs = cs + '0'
            N = N - 1
            cells = arr
            # print(cells)
            if cs not in di:
                di[cs] = 1
                ret.append(arr)
            else:
                break
        if N == 0:
            return cells 
        val = N%len(ret)
        return ret[val]
