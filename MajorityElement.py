class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mSize = len(nums)/2
        freq = {}
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 1
            else:
                freq[nums[i]] +=1
        for digit in freq:
            if freq[digit] > mSize:
                return digit
            
