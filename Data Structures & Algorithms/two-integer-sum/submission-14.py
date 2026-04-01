class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapped = {}
        for i, num in enumerate(nums):
            if target - num in mapped:
                return [mapped[target - num], i]
            mapped[num] = i