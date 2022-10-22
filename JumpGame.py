class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_step = nums[0]
        for i in range(1,len(nums)):
            if max_step < i:
                return False
            max_step = max(max_step, nums[i]+i)
        return True
