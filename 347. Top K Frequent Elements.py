class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for l in nums:
            res[l] = 1 + res.get(l, 0)
        sorted_res = sorted(res.keys(), key=lambda x: res[x], reverse=True)
        return sorted_res[:k]
        