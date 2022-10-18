class Solution:
    def combinationSum(self, candidates, target) :
        candidates.sort()
        res=[]
        def dfs(i,cur,total):
            if target==total:
                # cur.sort()
                if cur not in res:
                    res.append(cur.copy())
                return
            if i>=len(candidates) or total>target:
                return
            cur.append(candidates[i])
            dfs(i+1,cur,total+candidates[i])
            cur.pop()
            dfs(i+1,cur,total)
        dfs(0,[],0)
        res.sort()
        return res
sol = Solution()    
print(sol.combinationSum([2,5,2,1,2],5))