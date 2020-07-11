class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        ret = []
        subs = self.subsets(nums[1:])
        subs2 = []
        for s in subs:
            subs2.append([nums[0]]+s)
        ret = ret + subs + subs2
        return ret 