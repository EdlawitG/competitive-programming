class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        def swap(curr_idx, nxt_idx):
            nums[curr_idx], nums[nxt_idx] = nums[nxt_idx], nums[curr_idx]
        size = len(nums)
        for i in range(1, size -1):
            prev, cur, nxt = nums[i-1], nums[i], nums[i+1]
            if prev < cur < nxt or prev > cur > nxt:
                swap(i+1, i)
        return nums
        
