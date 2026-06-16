class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_set = {}
        for i,n in enumerate(nums):
            remainder = target -n
            if(remainder in nums_set):
                return [nums_set[remainder],i]
            nums_set[n]=i
        return []