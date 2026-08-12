class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        val = False
        if len(nums) <= 1:
            return True

        for i in range(len(nums)-1):
            if nums[i]%2 == nums[i+1]%2:
                val = False
                break
            else:
                val = True
        
        return val

            