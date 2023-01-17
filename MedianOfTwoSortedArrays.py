class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j, m, n, nums3 = 0, 0, len(nums1), len(nums2), []
        while(i<m and j<n):
            if(nums1[i]<=nums2[j]):
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1
        if i < m:
            for k in range(i,m,1):
                nums3.append(nums1[k])
        if j < n:
            for k in range(j,n,1):
                nums3.append(nums2[k])
        t = m+n
        if t%2==0:
            return (nums3[t//2] + nums3[t//2 -1])/2
        else:
            return nums3[t//2]
          """
          O(m+n) --> Brute Force  
            
          """
          
