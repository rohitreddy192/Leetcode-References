class Solution:
    def rob(self, nums: List[int]) -> int:
        def f(dp,ind):

            if ind==0: return nums[ind]
            if ind<0: return 0
            if dp[ind] != -1: return dp[ind]
            pick = nums[ind] + f(dp,ind-2)

            notPick = f(dp,ind-1)

            dp[ind] = max(pick,notPick)
            return dp[ind]
        dp = [-1 for i in range(len(nums))]
        dp[0] = nums[0]
        return f(dp,len(nums)-1)











class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            pick = nums[i]
            if i>1:
                pick += dp[i-2]
            notPick = dp[i-1]
            dp[i] = max(pick, notPick)
        return max(dp)
