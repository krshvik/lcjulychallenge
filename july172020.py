class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        di = {}
        for n in nums:
            if n in di:
                di[n] = di[n] + 1
            else:
                di[n] = 1
        rdi = {}
        for d in di:
            if di[d] in rdi:
                rdi[di[d]].append(d)
            else:
                rdi[di[d]] = [d]
        ret = []
        while len(ret) < k:
            maxc = max(rdi)
            ret = ret + rdi[maxc]
            del rdi[maxc]
        return ret 