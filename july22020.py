class Solution:
    
    di = {}
    
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        self.di = {}
        arr = []
        self.travel(root,0)
        while len(self.di) > 0:
            maxi = max(self.di)
            arr.append(self.di[maxi])
            del self.di[maxi]
        return arr 
    
    def travel(self,cnode,clvl):
        if cnode is None:
            return
        
        self.travel(cnode.left,clvl+1)
        if clvl not in self.di:
            self.di[clvl] = []
        
        self.di[clvl].append(cnode.val)
        self.travel(cnode.right,clvl+1)
        
        return 