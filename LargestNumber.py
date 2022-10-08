class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = sorted([str(x) for x in nums],reverse=True) 
        for i in range(len(nums)): 
            swapped = False
            for j in range(len(nums)-i-1):
                if len(nums[j]) == len(nums[j+1]):
                    continue
                    if int(nums[j]+nums[j+1]) < int(nums[j+1]+nums[j]):
                        nums[j],nums[j+1]=nums[j+1],nums[j]
                        swapped = True
            if not swapped:
                break
        ans = str(int("".join(nums))) 
        return ans
