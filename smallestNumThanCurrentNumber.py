class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        smallList = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if j!= i:
                    if nums[i] > nums[j]:
                        count +=1
            smallList.append(count)
        return smallList
        
