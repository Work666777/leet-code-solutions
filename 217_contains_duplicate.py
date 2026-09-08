class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mapdew = set()
        for number in nums:
            if number in mapdew:
                return True
            elif number not in mapdew:
                mapdew.add(number)
        else:
            return False