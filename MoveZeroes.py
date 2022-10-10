class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_num = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_num] = nums[i]
                last_num +=1
        for i in range(last_num, len(nums)):
            nums[i] = 0
            
