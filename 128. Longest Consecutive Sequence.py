# first try:
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       # while ii < len(nums):
        # ii = 0  
        res = {}
        ii = 0
        nums = sorted(nums)
        for i, n in enumerate(nums):
            #if int(i) < len(nums):
            if i + 1 < len(nums):
                if (nums[i] == nums[i+1]) or (i > 0 and nums[i] == nums[i-1]):
                    continue
                
                #if nums[i] == nums[i+1] or nums[i-1]:
                    continue
                elif  nums[i] + 1 == nums[i+1]:
                    res[ii] += nums[i]
                elif nums[i] + 1 != nums[i+1]:
                    ii += 1
        return res
        
        # [1,2,3,4,5]  

# second try:
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for n in nums:
            length = 1
            if n - 1 not in nums:
                while n + 1 in nums:
                    n += 1
                    length += 1
            longest = max(longest, length)
        return longest
    # solved