class Solution:
    def sortColors(self, nums: List[int]) -> None:
        def swap(a,b):
            nums[a], nums[b] = nums[b], nums[a]
        left,mid,right = 0,0,len(nums)-1
        while(mid<=right):
            if(nums[mid]==0):
                swap(mid,left)
                left+=1
                mid+=1
            elif(nums[mid]==1):
                mid+=1
            else:
                swap(mid,right)
                right-=1
                
                
                
        """
        sort 0, 1, 2 in array
        
        """
        
