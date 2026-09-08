class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
     prewMap = {}
     for i, n in enumerate(nums):
        diff = target - n
        if diff in prewMap:
            return [prewMap[diff], i]
        prewMap[n] = i