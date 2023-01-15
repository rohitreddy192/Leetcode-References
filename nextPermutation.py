class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        def swap(nums,i,j):
            nums[i], nums[j] = nums[j], nums[i]
        def reverse(nums,i,j):
            while(i<j):
                swap(nums,i,j)
                i += 1
                j -= 1
        if len(nums)<=1: return
        i = len(nums)-2
        while(i>=0 and nums[i]>=nums[i+1]): i-=1
        if(i>=0):
            j = len(nums)-1
            while(nums[j]<=nums[i]): j-=1
            swap(nums,i,j)
        reverse(nums,i+1,len(nums)-1)
        
