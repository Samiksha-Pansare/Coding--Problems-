class Solution:
    def subsets(self,nums):
        res, path =[], []
        self.dfs(0,res,path,nums)
        return res
    def dfs(self,inex,res,path,nums):
        res.append(list(path))
        for i in range(0,len(nums)):
            path.append(nums[i])
            self.dfs(i+1, res, path, nums)
            path.pop()

nums = [3,1,2,4]
sol= Solution()
sol.subsets(nums)