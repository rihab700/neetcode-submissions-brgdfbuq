class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapped = {}
        for i in range(len(nums)):
            r = target - nums[i]
            if r in mapped:
                return [mapped[r],i]

            else:
                mapped[nums[i]] = i