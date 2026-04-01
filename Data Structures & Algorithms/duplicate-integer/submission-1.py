class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapped = {}
        for i in range(len(nums)):
            if nums[i] in mapped:
                return True
            else:
                mapped[nums[i]]=i
        return False
            