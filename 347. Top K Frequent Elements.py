class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for l in nums:
            res[l] = 1 + res.get(l, 0)
        sorted_res = sorted(res.keys(), key=lambda x: res[x], reverse=True)
        return sorted_res[:k]


        # or more efficient solution 

    class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        fre = [[] for i in rane(len(nums)), + 1]

        for n in nums:
            count[n] = 1+ count.get(n, 0)
        for n, c in count.items():
                fre[c].append[n]
                

        res = []
        for i in range(len(fre) -1, 0, -1):
            for n in fre[i]:
                res.append[n]
                if len(res) == k:
                    return res
