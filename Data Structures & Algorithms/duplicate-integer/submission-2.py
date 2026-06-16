class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for x in nums:
            if x in seen:
                pass
            seen.add(x)
        if len(seen) == len(nums):
            return False
        else:
            return True
        
        