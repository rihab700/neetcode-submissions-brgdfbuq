class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = {}
        for i,n in enumerate(nums):
            if n in dup.values():
                return True
            dup[i]=n
        return False
        