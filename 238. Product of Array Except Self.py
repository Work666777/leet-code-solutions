### first try -__-

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count = []
        for  i, n in enumerate(nums):
            for n in nums[i:]:
               if nums[n+1] in nums:
                 h = nums[n] * nums[n+1]
                
            count.append(h)
            for n in nums[:i]:
                hh = nums[n] * nums[n-1]
            count.append(hh)

            res = []
            
            s = count[hh] * count[h]
            res.append[s]
            return res

           ### product = nums[i+1] * nums[i+1:] * nums[i-1] * nums[:i-1]
          ### count.append[product]


        ### return count


        class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            count[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(len(nums) -1, -1, -1):
            count[i] *= suffix
            suffix *= nums[i]