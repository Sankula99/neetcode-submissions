class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # we can check the length of the set(since set holds one copy of each value) against the length of the list
        return len(set(nums))< len(nums)