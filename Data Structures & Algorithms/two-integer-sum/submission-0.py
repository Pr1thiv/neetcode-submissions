class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for index, element in enumerate(nums):
            diff = target - element
            if diff in prevMap:
                return [prevMap[diff],index]
            
            prevMap[element] = index
        return
            