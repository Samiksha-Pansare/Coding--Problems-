class Solution:
    def combinationSum(self, candidates, target) :
        res=[]
        def dfs(i,cur,total):
            if target==total:
                res.append(cur.copy())
                return
            if i>=len(candidates) or total>target:
                return
            cur.append(candidates[i])
            dfs(i,cur,total+candidates[i])
            cur.pop()
            dfs(i+1,cur,total)
        dfs(0,[],0)
        return res
sol = Solution()    
print(sol.combinationSum([2,3,6,7],7))