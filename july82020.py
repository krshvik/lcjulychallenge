class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        di = {}
        for n in nums:
            if n in di:
                di[n] = di[n] + 1
            else:
                di[n] = 1

        if len(di) == 1 and 0 in di and di[0] > 2:
            return [[0, 0, 0]]

        res = {}

        while len(nums) > 2:
            i = nums[0]

            if di[i] > 1:
                di[i] = di[i] - 1
            else:
                del di[i]

            k = 1
            lenn = len(nums)
            while k < lenn:

                j = nums[k]

                if di[j] > 1:
                    di[j] = di[j] - 1
                else:
                    del di[j]

                if -i - j in di:
                    b = [i, j, -i - j]
                    b.sort()

                    if b[0] in res:
                        if b[1] in res[b[0]]:
                            if b[2] not in res[b[0]][b[1]]:
                                res[b[0]][b[1]][b[2]] = 1
                        else:
                            res[b[0]][b[1]] = {}
                            res[b[0]][b[1]][b[2]] = 1
                    else:
                        res[b[0]] = {}
                        res[b[0]][b[1]] = {}
                        res[b[0]][b[1]][b[2]] = 1

                if j in di:
                    di[j] = di[j] + 1
                else:
                    di[j] = 1

                k = k + 1

            del nums[0]

        ans = []
        for r in res:
            for s in res[r]:
                for t in res[r][s]:
                    ans.append([r, s, t])
        return ans