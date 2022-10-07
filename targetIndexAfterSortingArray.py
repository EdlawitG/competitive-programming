class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        targetIndex = []
        length = len(nums)
        for i in range(length-1):
            for j in range(i+1,length):
                if nums[i] > nums[j]:
                    nums[i],nums[j] = nums[j],nums[i]
        for i in range(length):
            if nums[i] == target:
                targetIndex.append(i)
        return targetIndex
