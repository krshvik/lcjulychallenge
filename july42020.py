class Solution:
    
    arr = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27, 30, 32, 36, 40, 45, 48, 50, 54, 60, 64]

    
    def nthUglyNumber(self, n: int) -> int:
        if n <= len(self.arr):
            return self.arr[n-1]
        
        val = self.arr[len(self.arr)-1] + 1
        lena = len(self.arr)
        while lena <= n:
            a = val 
            a1 = int(val//2)
            a2 = int(val//3)
            a3 = int(val//5)
            
            b1 = self.bsearch(a1,self.arr,0,lena-1)
            b2 = self.bsearch(a2,self.arr,0,lena-1)
            b3 = self.bsearch(a3,self.arr,0,lena-1)
            
            mini = min(self.arr[b1]*2,self.arr[b2]*3,self.arr[b3]*5)
            self.arr.append(mini)
            lena = lena + 1
            val = self.arr[lena-1]            
        print(self.arr)
        return self.arr[n-1]
    
    def bsearch(self,val,arr,l,r):
        
        mid = int((l+r)//2)
        if arr[mid] == val:
            return mid+1
        if arr[mid] > val:
            return self.bsearch(val,arr,l,mid-1)
        if arr[mid] < val:
            if arr[mid+1] > val:
                return mid + 1
            return self.bsearch(val,arr,mid+1,r)
        