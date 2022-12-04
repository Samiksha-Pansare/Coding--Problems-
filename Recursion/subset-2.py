class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        def backtrack(first = 0, curr = []):           
            # if the combination is done
            if len(curr) == k: 
                if curr not in output:
                    output.append(curr[:])
                return
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                print("ele: ",nums[i])
                print("Curr: ",curr)
                # use next integers to complete the combination
                backtrack(i+1, curr)
                # backtrack
                curr.pop()
                print("After pop Curr: ",curr)
        
        output = []
        n = len(nums)
        for k in range(n + 1):
            print("k=",k)
            backtrack()
        return output

sol= Solution()
nums=[4,1,0]
res=sol.subsetsWithDup(nums)
print("Result=",res)